#!/usr/bin/make -f

SUBDIRS := etc/xdg/xdg-xubuntu/Thunar/po etc/xdg/xdg-xubuntu/xfce4/whiskermenu/po usr/bin/po/ usr/share/xsessions/po usr/share/xubuntu/applications/po usr/share/xubuntu/templates/po

all:
	@echo "Nothing to build, call 'make install' instead."

generate-pot:
	for i in $(SUBDIRS); do \
		make -C $$i generate-pot; \
	done

install:
	mkdir -pv $(DESTDIR)
	cp -a etc usr $(DESTDIR)/.
	mkdir -pv $(DESTDIR)/usr/share/locale
	# po generation
	for i in $(SUBDIRS); do \
		make -C $(DESTDIR)/$$i; \
		rm -rf $(DESTDIR)/$$i; \
	done
	# remove some remaining files
	find $(DESTDIR) -type f -iname "*.in" | xargs rm -f

# vim:ts=4
