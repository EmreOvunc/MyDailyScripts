#!/bin/sh
sudo tail -n0 -f /var/log/messages | while read line; do notify-send "System Message" "$line" -i /usr/share/icons/Adwaita/32x32/emblems/emblem-important.png ;done

