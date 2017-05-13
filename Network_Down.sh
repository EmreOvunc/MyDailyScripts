sudo service networking stop
sudo service network-manager stop
sudo iptables -F
notify-send "Network" "Network Services are stopped!" -i /usr/share/icons/Adwaita/32x32/status/network-error.png & paplay /usr/share/sounds/KDE-Im-Contact-Out.ogg
