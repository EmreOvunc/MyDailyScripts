#!/bin/sh
sudo iptables -F
sudo iptables -A FORWARD -s 192.168.1.41 -i wlan0 -o vboxnet0 -d 10.0.0.210 -j ACCEPT
sudo iptables -A FORWARD -s 192.168.1.41 -i wlan0 -o vboxnet0 -d 10.0.0.210 -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
