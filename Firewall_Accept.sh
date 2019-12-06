notify-send "Firewall" "Now Unsecured!" -i /usr/share/icons/Adwaita/32x32/status/dialog_warning.png & /usr/share/sounds/KDE-Im-Error-On-Connection.ogg
sudo iptables -F
sudo iptables -P INPUT ACCEPT
sudo iptables -P OUTPUT ACCEPT
sudo iptables -P FORWARD ACCEPT
