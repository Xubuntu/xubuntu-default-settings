#!/usr/bin/make -f

POTFILES := uca.xml.in

RELEASE := jaunty

all: generate-uca

generate-pot: POTFILES.in
	intltool-update --pot --gettext-package=thunar-uca-$(RELEASE)

generate-uca: *.po
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -x . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=thunar-uca-$(RELEASE) --dist $$code; \
	done

# vim:ts=4
