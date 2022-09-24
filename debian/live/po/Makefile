#!/usr/bin/make -f

POTFILES := whiskermenu-1.rc.in

all: generate-whiskermenu-1

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=whiskermenu-1

generate-whiskermenu-1:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=whiskermenu-1 --dist $$code; \
	done

# vim:ts=4
