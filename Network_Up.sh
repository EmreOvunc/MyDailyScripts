sudo service networking start
sudo service network-manager start
sh /home/monster/Scripts/Emre_Firewall.sh
notify-send "Network" "Network Services are started!" -i /usr/share/icons/Adwaita/32x32/status/network-transmit-receive.png & paplay /usr/share/sounds/KDE-Im-Contact-In.ogg
