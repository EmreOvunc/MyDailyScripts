sudo iptables -t nat -F
sudo iptables -F
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination 10.0.1.1:80
sudo iptables -t nat -A POSTROUTING -p tcp -d 10.0.1.1 --dport 80 -j SNAT --to-source 192.168.45.135
sudo sysctl net.ipv4.ip_forward=1
