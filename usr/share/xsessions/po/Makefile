#!/usr/bin/make -f

POTFILES := xubuntu.desktop.in

all: generate-xsession-file

generate-headers:
	rm -f POTFILES.in
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in/\.in\.h/'); \
		intltool-extract -l --type=gettext/ini ../$$i; \
		echo "$$f" | tee -a POTFILES.in; \
	done

generate-pot: generate-headers
	xgettext --directory=tmp --files-from=POTFILES.in --output=xubuntu-xsession-file.pot --keyword=_ --keyword=N_ --keyword=Q_ --from-code=UTF-8
	rm -rf tmp POTFILES.in

generate-xsession-file:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=xubuntu-xsession-file --dist $$code; \
	done

# vim:ts=4
