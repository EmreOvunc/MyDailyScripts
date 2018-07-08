sudo iptables -t nat -F
sudo iptables -F
MY="10.0.1.143"
DST="10.70.50.1"
sudo iptables -t nat -A PREROUTING -p tcp --dport 80 -j DNAT --to-destination $DST:80
sudo iptables -t nat -A POSTROUTING -p tcp -d $DST --dport 80 -j SNAT --to-source $MY
sudo sysctl net.ipv4.ip_forward=1
