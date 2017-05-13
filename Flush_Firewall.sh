#!/bin/sh
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
sudo iptables -F
notify-send "Firewall" "Rules are flushed!" -i /usr/share/icons/Adwaita/32x32/status/changes-allow.png & paplay /usr/share/sounds/KDE-Im-Error-On-Connection.ogg
