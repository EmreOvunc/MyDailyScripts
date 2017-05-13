sudo iptables -F
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -A INPUT -p udp -s 192.168.1.0/24 --dport 137 -j ACCEPT
sudo iptables -A INPUT -p udp -s 192.168.1.0/24 --dport 138 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 139 -j ACCEPT
sudo iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 445 -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -p udp --sport 137:138 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -p tcp --sport 139 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -p tcp --sport 445 -m state --state ESTABLISHED -j ACCEPT
