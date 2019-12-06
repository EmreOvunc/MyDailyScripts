
#!/bin/sh
HOME="192.168.1.0/24"
iptables -F
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i eth0 -p udp -m udp --sport 53 -j ACCEPT
iptables -A OUTPUT -o eth0 -p udp -m udp --dport 53 -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
##
iptables -A INPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A INPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
##
iptables -A INPUT -i eth0 -s $HOME -p tcp -m mac --mac-source AA:BB:CC:11:22:33 --dport 2222 -j ACCEPT
iptables -A OUTPUT -o eth0 -d $HOME -p tcp --sport 2222 -j ACCEPT
##
iptables -A INPUT -i eth0 -p udp -s $HOME --dport 137 -j ACCEPT
iptables -A INPUT -i eth0 -p udp -s $HOME --dport 138 -j ACCEPT
iptables -A INPUT -i eth0 -p tcp -s $HOME --dport 139 -j ACCEPT
iptables -A INPUT -i eth0 -p tcp -s $HOME --dport 445 -j ACCEPT
iptables -A OUTPUT -o eth0 -d $HOME -p tcp --sport 139 -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -d $HOME -p tcp --sport 445 -m state --state ESTABLISHED -j ACCEPT
iptables -A OUTPUT -o eth0 -d $HOME -p udp --sport 137:138 -m state --state ESTABLISHED -j ACCEPT
##
iptables-save
##
