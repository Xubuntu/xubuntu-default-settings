#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vi: set ft=python :
"""
Launchpad Bug Tracker uses launchpadlib to get the bugs.

Based on https://github.com/ubuntu/yaru/blob/master/.github/lpbugtracker.py
"""

import os
import subprocess
import logging
from launchpadlib.launchpad import Launchpad

log = logging.getLogger("lpbugtracker")
log.setLevel(logging.DEBUG)

GH_OWNER = "bluesabre"
GH_REPO = "xubuntu-default-settings"

LP_SOURCE_NAME = "xubuntu-default-settings"
LP_SOURCE_URL_NAME = "xubuntu-default-settings"

HOME = os.path.expanduser("~")
CACHEDIR = os.path.join(HOME, ".launchpadlib", "cache")


def main():
    lp_bugs = get_lp_bugs()
    if len(lp_bugs) == 0:
        return

    gh_bugs = get_gh_bugs()

    for id in lp_bugs:
        if id in gh_bugs.keys():
            gh_labels = parse_gh_labels(gh_bugs[id]["labels"])
            if lp_bugs[id]["closed"] and gh_bugs[id]["status"] != "closed":
                close_issue(gh_bugs[id]["id"], gh_labels["labels"], lp_bugs[id]["status"])
            elif lp_bugs[id]["status"] != gh_labels["status"]:
                update_issue(gh_bugs[id]["id"], gh_labels["labels"], lp_bugs[id]["status"])
        elif not lp_bugs[id]["closed"] and lp_bugs[id]["status"] != "Incomplete":
            create_issue(id, lp_bugs[id]["title"], lp_bugs[id]["link"], lp_bugs[id]["status"])


def get_lp_bugs():
    """Get a list of bugs from Launchpad"""

    lp = Launchpad.login_anonymously(
        "%s LP bug checker" % LP_SOURCE_NAME, "production", CACHEDIR, version="devel"
    )

    ubuntu = lp.distributions["ubuntu"]
    archive = ubuntu.main_archive

    packages = archive.getPublishedSources(source_name=LP_SOURCE_NAME)
    package = ubuntu.getSourcePackage(name=packages[0].source_package_name)

    bug_tasks = package.searchTasks(status=["New", "Opinion",
                                            "Invalid", "Won't Fix",
                                            "Expired", "Confirmed",
                                            "Triaged", "In Progress",
                                            "Fix Committed", "Fix Released",
                                            "Incomplete"])
    bugs = {}

    for task in bug_tasks:
        id = str(task.bug.id)
        title = task.title.split(": ")[1]
        status = task.status
        closed = status in ["Invalid", "Won't Fix", "Expired", "Fix Released"]
        link = "https://bugs.launchpad.net/ubuntu/+source/{}/+bug/{}".format(LP_SOURCE_URL_NAME, id)
        bugs[id] = {"title": title, "link": link, "status": status, "closed": closed}

    return bugs


def get_gh_bugs():
    """Get the list of the LP bug already tracked in GitHub.

    Launchpad bugs tracked on GitHub have a title like

    "LP#<id> <title>"

    this function returns a list of the "LP#<id>" substring for each bug,
    open or closed, found on the repository on GitHub.
    """

    output = subprocess.check_output(
        ["hub", "issue", "--labels", "Launchpad", "--state", "all", "--format", "%I|%S|%L|%t%n"]
    )
    bugs = {}
    for line in output.decode().split("\n"):
        if "LP#" in line:
            id, status, labels, lp = line.strip().split("|", 3)
            labels = labels.split(", ")
            lpid, title = lp.split(" ", 1)
            lpid = lpid[3:]
            bugs[lpid] = {"id": id, "status": status, "title": title, "labels": labels}
    return bugs


def parse_gh_labels(labels):
    result = {
        "status": "Unknown",
        "labels": []
    }
    for label in labels:
        if label == "Launchpad":
            continue
        elif label in ["New", "Opinion",
                       "Invalid", "Won't Fix",
                       "Expired", "Confirmed",
                       "Triaged", "In Progress",
                       "Fix Committed", "Fix Released",
                       "Incomplete"]:
            result["status"] = label
        else:
            result["labels"].append(label)
    return result


def create_issue(id, title, weblink, status):
    """ Create a new Bug using HUB """
    print("creating:", id, title, weblink, status)
    subprocess.run(
        [
            "hub",
            "issue",
            "create",
            "--message",
            "LP#{} {}".format(id, title),
            "--message",
            "Reported first on Launchpad at {}".format(weblink),
            "-l",
            "Launchpad,%s" % status,
        ]
    )


def update_issue(id, current_labels, status):
    """ Create a new Bug using HUB """
    print("updating:", id, status)

    new_labels = ["Launchpad", status] + current_labels

    subprocess.run(
        [
            "hub",
            "issue",
            "update",
            "-l",
            ",".join(new_labels),
        ]
    )


def close_issue(id, current_labels, status):
    """ Close the Bug using HUB and leave a comment """
    print("closing:", id, status)

    new_labels = ["Launchpad", status] + current_labels

    subprocess.run(
        [
            "hub",
            "api",
            "repos/{}/{}/issues/{}/comments".format(GH_OWNER, GH_REPO, id),
            "--field",
            "body=Issue closed on Launchpad with status: {}".format(status)
        ]
    )

    subprocess.run(
        [
            "hub",
            "issue",
            "update",
            id,
            "--state",
            "closed",
            "-l",
            ",".join(new_labels),
        ]
    )


if __name__ == "__main__":
    main()
