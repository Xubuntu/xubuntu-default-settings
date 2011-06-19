#!/bin/sh
# Copyright © 2010-2011 Lionel Le Folgoc <mrpouit@ubuntu.com>

# Add the default XDG config dir, as it's not done automatically by lightdm yet
if [ -z "$XDG_CONFIG_DIRS" ]; then
  XDG_CONFIG_DIRS="/etc/xdg/xdg-xubuntu"
fi
export XDG_CONFIG_DIRS="/etc/xdg/xdg-xubuntu:$XDG_CONFIG_DIRS"

# Readd /usr/local/share, as startxfce4 adds it only if $XDG_DATA_DIRS is empty
if [ -z "$XDG_DATA_DIRS" ]; then
  XDG_DATA_DIRS="/usr/local/share"
fi
export XDG_DATA_DIRS="/usr/share/xubuntu:$XDG_DATA_DIRS"

exec startxfce4
