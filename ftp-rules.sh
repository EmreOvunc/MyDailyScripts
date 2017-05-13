SERVER_IP = "SERVERIP"
sudo iptables -F
sudo iptables -P OUTPUT DROP
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -A OUTPUT -d $SERVER_IP -p tcp --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -s $SERVER_IP -p tcp --sport 21 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $SERVER_IP -p tcp --sport 1024: --dport 1024: -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -s $SERVER_IP -p tcp --sport 1024: --dport 1024: -m state --state ESTABLISHED -j ACCEPT
