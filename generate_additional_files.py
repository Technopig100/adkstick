#!/usr/bin/python3

DOMAIN = "adkstick"
PATH = "/usr/share/linuxadk/locale"

import os, gettext
from adkcommon import additionalfiles

os.environ['LANGUAGE'] = "en_US.UTF-8"
gettext.install(DOMAIN, PATH)

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=adkstick
Exec=adkstick -m iso
Categories=GNOME;GTK;Utility;
NotShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/adkstick.desktop", prefix, _("USB Image Writer"), _("Make a bootable USB stick"), "")

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=system-run
Exec=adkstick -m iso
Categories=System;
OnlyShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/adkstick-kde.desktop", prefix, _("USB Image Writer"), _("Make a bootable USB stick"), "", genericName=_("Make a bootable USB stick"))

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=adkstick
Exec=adkstick -m format
Categories=GNOME;GTK;Utility;
NotShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/adkstick-format.desktop", prefix, _("USB Stick Formatter"), _("Format a USB stick"), "")

prefix = """[Desktop Entry]
Version=1.0
Type=Application
Terminal=false
Icon=system-run
Exec=adkstick -m format
Categories=System;
OnlyShowIn=KDE;
"""

additionalfiles.generate(DOMAIN, PATH, "share/applications/adkstick-format-kde.desktop", prefix, _("USB Stick Formatter"), _("Format a USB stick"), "", genericName=_("Format a USB stick"))

prefix="""[Nemo Action]
Active=true
Exec=adkstick -m iso -i "%F"
Icon-Name=media-removable-symbolic
Selection=S
Extensions=iso;img;
"""
additionalfiles.generate(DOMAIN, PATH, "share/nemo/actions/adkstick.nemo_action", prefix, _("Make bootable USB stick"), _("Make a bootable USB stick"), "")

prefix="""[Nemo Action]
Active=true
Exec=adkstick -m format -u %D
Icon-Name=edit-clear-all-symbolic
Selection=S
Extensions=any;
Conditions=removable;
"""
additionalfiles.generate(DOMAIN, PATH, "share/nemo/actions/adkstick-format.nemo_action", prefix, _("Format"), _("Format a USB stick"), "")

prefix="""<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE policyconfig PUBLIC
 "-//freedesktop//DTD PolicyKit Policy Configuration 1.0//EN"
 "http://www.freedesktop.org/standards/PolicyKit/1/policyconfig.dtd">
<policyconfig>

  <vendor>Linux adk</vendor>
  <vendor_url>https://linuxadk.com</vendor_url>

  <action id="com.linuxadk.adkstick">
    <description>USB Image Writer / USB Stick Formatter</description>
"""

suffix="""
    <icon_name>adkstick</icon_name>
    <defaults>
      <allow_any>no</allow_any>
      <allow_inactive>no</allow_inactive>
      <allow_active>auth_admin_keep</allow_active>
    </defaults>
    <annotate key="org.freedesktop.policykit.exec.path">/usr/bin/python3</annotate>
    <annotate key="org.freedesktop.policykit.exec.argv1">/usr/lib/adkstick/raw_write.py</annotate>
    <annotate key="org.freedesktop.policykit.exec.argv1">/usr/lib/adkstick/raw_format.py</annotate>
    <annotate key="org.freedesktop.policykit.exec.allow_gui">true</annotate>
  </action>

</policyconfig>
"""

additionalfiles.generate_polkit_policy(DOMAIN, PATH, "share/polkit/com.linuxadk.adkstick.policy", prefix, _("This will destroy all data on the USB stick, are you sure you want to proceed?"), suffix)

