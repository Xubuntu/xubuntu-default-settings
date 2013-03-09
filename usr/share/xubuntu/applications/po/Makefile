#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-xds-desktop-files

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=xds-desktop-files

generate-xds-desktop-files:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=xds-desktop-files --dist $$code; \
	done

# vim:ts=4
