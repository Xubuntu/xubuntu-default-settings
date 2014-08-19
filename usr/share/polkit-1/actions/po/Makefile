#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-xds-polkit-files

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=xds-polkit-files

generate-xds-polkit-files:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge --xml-style . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=xds-polkit-files --dist $$code; \
	done

# vim:ts=4
