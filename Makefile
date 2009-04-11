#!/usr/bin/make -f

SUBDIRS := etc/xdg/xubuntu/xfce4/panel/po

all: install

install:
	cp -a etc usr $(DESTDIR)/.
	# po generation
	for i in $(SUBDIRS); do \
		make -C $(DESTDIR)/$$i; \
		rm -rf $(DESTDIR)/$$i; \
	done
	# remove some remaining files
	find $(DESTDIR) -type f -iname "*.in" | xargs rm -f

# vim:ts=4
