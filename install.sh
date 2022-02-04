#!/bin/sh
#
#    Copyright 2007-2009 Canonical Ltd.
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License as
#  published by the Free Software Foundation; either version 2 of the
#  License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301, USA

LIBFILES="adkstick.py raw_write.py raw_format.py mountutils.py"
DATAFILES="adkstick.glade adkstick.ui"


if [ "$1" = "uninstall" ]; then
    rm -rf /usr/lib/adkstick
    rm -rf /usr/share/adkstick
    rm -r /usr/share/applications/adkstick.desktop
    rm -r /usr/share/applications/adkstick-kde.desktop
    rm -r /usr/share/applications/adkstick-format.desktop
    rm -r /usr/share/applications/adkstick-kde-format.desktop
    rm -f /usr/bin/adkstick
    rm -rf /usr/share/polkit-1/actions/org.linuxmint.im.policy
    rm -rf /usr/share/kde4/apps/solid/actions/adkstick-format.desktop
else
    cp share/applications/adkstick.desktop /usr/share/applications/
    cp share/applications/adkstick-format.desktop /usr/share/applications/
    cp share/applications/adkstick-kde.desktop /usr/share/applications/
    cp share/applications/adkstick-format-kde.desktop /usr/share/applications/
    cp share/polkit/org.linuxmint.im.policy /usr/share/polkit-1/actions
    cp share/kde4/adkstick-format_action.desktop /usr/share/kde4/apps/solid/actions
    cp adkstick /usr/bin/
    mkdir -p /usr/lib/adkstick
    mkdir -p /usr/share/adkstick

    for item in $LIBFILES; do
        cp lib/$item /usr/lib/adkstick/
    done

    for item in $DATAFILES; do
        cp share/adkstick/$item /usr/share/adkstick/
    done
fi
