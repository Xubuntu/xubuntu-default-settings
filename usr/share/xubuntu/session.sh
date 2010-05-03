#!/bin/sh
# Copyright © 2010 Lionel Le Folgoc <mrpouit@ubuntu.com>

# Readd /usr/local/share, as startxfce4 adds it only if $XDG_DATA_DIRS is empty
if [ -z "$XDG_DATA_DIRS" ]; then
  XDG_DATA_DIRS="/usr/local/share"
fi
export XDG_DATA_DIRS="/etc/xdg/xdg-xubuntu:$XDG_DATA_DIRS"

exec startxfce4
