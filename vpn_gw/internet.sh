sudo iptables -t nat -F
sudo iptables -F
sudo sysctl net.ipv4.ip_forward=1
sudo rm -rf /etc/resolv.conf
sudo echo "nameserver 1.1.1.1" > resolv.conf
sudo echo "nameserver 8.8.8.8" >> resolv.conf
sudo echo "nameserver 208.67.222.222" >> resolv.conf
sudo echo "nameserver 8.8.4.4" >> resolv.conf
sudo echo "nameserver 208.67.222.220" >> resolv.conf
sudo mv resolv.conf /etc/resolv.conf
sudo iptables -A FORWARD --in-interface eth0 -j ACCEPT
sudo iptables -t nat -A POSTROUTING -o wlan1 -j MASQUERADE
sudo iptables -A INPUT -i wlan1 -p tcp --dport 443 -j DROP
sudo iptables -A INPUT -i wlan1 -p tcp --dport 80 -j DROP
sudo iptables -A INPUT -i wlan1 -p tcp --dport 22 -j DROP
sudo iptables -A INPUT -i wlan1 -p udp --dport 53 -j DROP
