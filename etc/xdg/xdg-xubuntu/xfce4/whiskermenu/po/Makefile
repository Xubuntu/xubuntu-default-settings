#!/usr/bin/make -f

POTFILES := defaults.rc.in

all: generate-whiskermenu

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=whiskermenu

generate-whiskermenu:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=whiskermenu --dist $$code; \
	done

# vim:ts=4
