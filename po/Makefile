#!/usr/bin/make -f

RELEASE := jaunty
POTFILES := POTFILES.in

generate-pot:
	intltool-update --pot --gettext-package=xubuntu-default-settings.$(RELEASE)

merge-po: $(foreach p,$(shell read $(POTFILES)),merge-po-$(p))
merge-po-%:
	intltool-merge . $(*) $(subst .in,,$(*))

update-po:
	intltool-update
