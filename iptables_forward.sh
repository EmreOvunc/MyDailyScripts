sysctl net.ipv4.ip_forward=1
dst_ip="1.1.1.1"
iptables -t nat -A PREROUTING -p tcp --dport 139 -j DNAT --to $dst_ip:139
iptables -A FORWARD -d $dst_ip -p tcp --dport 139 -j ACCEPT
iptables -t nat -A PREROUTING -p tcp --dport 445 -j DNAT --to $dst_ip:445
iptables -A FORWARD -d $dst_ip -p tcp --dport 445 -j ACCEPT