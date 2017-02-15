#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-locales

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=xdg-xubuntu-templates

generate-locales:
	for i in $$(find $$1 -name *.po); do \
		code=$$(echo $$i | sed 's/.po//'); \
		mkdir -p locale/$$code/LC_MESSAGES/; \
    msgfmt -o locale/$$code/LC_MESSAGES/xdg-xubuntu-templates.mo $$i; \
	done; \
	mv locale ../../../

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=xdg-xubuntu-templates --dist $$code; \
	done

# vim:ts=4
