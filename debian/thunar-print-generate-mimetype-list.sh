#!/usr/bin/env bash

# This simple script echoes all valid file extensions for the usr/bin/thunar-print
# custom action script.
# As capabilities of CUPS may differ, this script should ideally be run to populate the
# corresponding <patterns> node in etc/xdg/xdg-xubuntu/Thunar/uca.xml.in
# The contents of this node are currently hardcoded based on the output of this script.

# Authors: Simon Steinbeiß <simon@xfce.org>
#          Florian Schüller <florian.schueller@gmail.com>

MIMETYPES=$(cat /usr/share/cups/mime/cupsfilters.convs|grep -Po "^[^#\t]+"|while read mime;do grep "^$mime" /etc/mime.types ;done|grep -Po "\t.*$")
LO_MIMETYPES=$(cat /usr/share/mime-info/libreoffice.mime|grep -Po "(?<=ext: ).*"|sort|uniq)

for ext in $MIMETYPES $LO_MIMETYPES; do
  echo $ext;
done|sort|uniq|while read ext; do
  echo -n ",*.$ext";
done|tail -c +2
echo
