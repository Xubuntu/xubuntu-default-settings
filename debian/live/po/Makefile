#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-desktop-provision-slides

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=desktop-provision-slides

generate-desktop-provision-slides:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=desktop-provision-slides --dist $$code; \
	done

# vim:ts=4