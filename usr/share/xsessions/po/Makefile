#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-xds-xsession-files

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=xds-xsession-files

generate-xds-xsession-files:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=xds-xsession-files --dist $$code; \
	done

# vim:ts=4