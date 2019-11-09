#!/usr/bin/make -f

POTFILES := $(shell cat POTFILES.in)

all: generate-locales

generate-pot: POTFILES.in
	xgettext -o thunar-print.pot  -L Shell --keyword --keyword=eval_gettext ../thunar-print

generate-locales:
	for i in $$(find $$1 -name "*.po"); do \
		code=$$(echo $$i | sed 's/.po//'); \
		mkdir -p locale/$$code/LC_MESSAGES/; \
	msgfmt -o locale/$$code/LC_MESSAGES/thunar-print.mo $$i; \
	done; \
	cp -R locale/* ../../share/locale

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=thunar-print --dist $$code; \
	done

# vim:ts=4
