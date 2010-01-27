#!/bin/sh
# Copyright © 2010 Lionel Le Folgoc <mrpouit@ubuntu.com>

# Simple wrapper to set XDG base dirs to some values
export XDG_CONFIG_DIRS=/etc/xdg/xdg-xubuntu
export XDG_DATA_DIRS=/etc/xdg/xdg-xubuntu
exec startxfce4
