#!/usr/bin/make -f

POTFILES := places-2.rc.in \
			launcher-2.rc.in \
			xfce4-menu-1.rc.in \
			launcher-3.rc.in

RELEASE := jaunty

all: generate-rc-files

generate-headers:
	rm -f POTFILES.in
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in/\.in\.h/'); \
		intltool-extract -l --type=gettext/ini ../$$i; \
		echo "$$f" | tee -a POTFILES.in; \
	done

generate-pot: generate-headers
	xgettext --directory=tmp --files-from=POTFILES.in --output=panel-rc-files-$(RELEASE).pot --keyword=_ --keyword=N_ --keyword=Q_ --from-code=UTF-8
	rm -rf tmp POTFILES.in

generate-rc-files:
	for i in $(POTFILES); do \
		f=$$(echo $$i | sed 's/\.in//'); \
		intltool-merge -d . ../$$i ../$$f; \
	done

update-po:
	for i in *.po; do \
		code=$$(echo $$i | sed 's/.po//'); \
		intltool-update --gettext-package=panel-rc-files-$(RELEASE) --dist $$code; \
	done

# vim:ts=4
