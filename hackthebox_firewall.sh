#!/bin/bash
#HackTheBox IPTables Firewall
#EmreOvunc 
#
ETHERNET="eth0"
INTERNAL="192.168.0.0/16"
OPENVPN="tun0"
MACHINES="10.10.10.0/24"
#
iptables -F
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD DROP
#
iptables -A INPUT -i lo -j ACCEPT
iptables -A INPUT -i $ETHERNET -j ACCEPT
iptables -A INPUT -s 127.0.0.0/16 -j ACCEPT
iptables -A INPUT -p udp --sport 53 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --sport 80 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --sport 443 -j ACCEPT
iptables -A INPUT -i $OPENVPN -p udp -s $MACHINES -j ACCEPT
iptables -A INPUT -i $OPENVPN -m tcp -p tcp -s $MACHINES -j ACCEPT
iptables -A INPUT -i $OPENVPN -p tcp -s $MACHINES --dport 139 -j ACCEPT
iptables -A INPUT -i $OPENVPN -p tcp -s $MACHINES --dport 445 -j ACCEPT
iptables -A INPUT -i $OPENVPN -p tcp -s $MACHINES --dport 8000 -j ACCEPT
iptables -A INPUT -i $OPENVPN -s $MACHINES -m tcp -p tcp --dport 4444 -j ACCEPT
iptables -A INPUT -i $OPENVPN -s $MACHINES -m tcp -p tcp --dport 4545 -j ACCEPT
#
iptables -A FORWARD -i $ETHERNET -s $INTERNAL -j ACCEPT
iptables -A FORWARD -o $ETHERNET -d $INTERNAL -j ACCEPT
#
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A OUTPUT -o $ETHERNET -j ACCEPT
iptables -A OUTPUT -d 127.0.0.0/16 -j ACCEPT
iptables -A OUTPUT -p udp --dport 53 -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 80 -j ACCEPT
iptables -A OUTPUT -p tcp -m tcp --dport 443 -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -p udp -d $MACHINES -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -m tcp -p tcp -d $MACHINES -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -p tcp -d $MACHINES --sport 139 -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -p tcp -d $MACHINES --sport 445 -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -p tcp -d $MACHINES --sport 8000 -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -d $MACHINES -m tcp -p tcp --sport 4444 -j ACCEPT
iptables -A OUTPUT -o $OPENVPN -d $MACHINES -m tcp -p tcp --sport 4545 -j ACCEPT
#
iptables-save