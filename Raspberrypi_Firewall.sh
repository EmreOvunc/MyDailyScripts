#!/bin/sh
sudo iptables -F
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT DROP
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A INPUT -i wlan0 -p udp -m udp --sport 53 -j ACCEPT
sudo iptables -A INPUT -i eth0 -p udp -m udp --sport 53 -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -s 192.168.1.254 -i eth0 -p tcp -m tcp --dport 2222 -j ACCEPT
sudo iptables -A INPUT -s 192.168.1.254 -i wlan0 -p tcp -m tcp --dport 2222 -m mac --mac-source AA:BB:CC:11:22:33 -j ACCEPT
sudo iptables -A INPUT -s 10.0.0.1 -i eth0 -p tcp -m tcp --dport 2222 -j ACCEPT
sudo iptables -A OUTPUT -o eth0 -p udp -m udp --dport 53 -j ACCEPT
sudo iptables -A OUTPUT -o wlan0 -p udp -m udp --dport 53 -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.254 -o eth0 -p tcp -m tcp --sport 2222 -j ACCEPT
sudo iptables -A OUTPUT -d 192.168.1.0/24 -o wlan0 -p tcp -m tcp --sport 2222 -j ACCEPT
sudo iptables -A OUTPUT -d 10.0.0.1 -o eth0 -p tcp -m tcp --sport 2222 -j ACCEPT
sudo iptables-save
