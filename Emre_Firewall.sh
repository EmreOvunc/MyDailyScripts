#!/bin/sh
######################
#IP LIST FOR FIREWALL
VIRTUAL="VIRTUALSIP"
ANOTHER_HOST="ANOTHERIP"
HOME="192.168.1.0/24"
MY_SERVER="SERVERIP"
MY_HOSTING="SERVERIP"
MUTE_SERVER="SERVERIP"
PORTS="PORTS"
######################
#FLUSH FIREWALL
sudo iptables -F
######################
#DROP EVERY CHAIN
sudo iptables -P INPUT DROP
sudo iptables -P OUTPUT DROP
sudo iptables -P FORWARD DROP
######################
#LOCALHOST
sudo iptables -A INPUT -i lo -j ACCEPT
sudo iptables -A OUTPUT -o lo -j ACCEPT
######################
#DNS COMMUNICATIONS
sudo iptables -A INPUT -i enp3s0 -p udp -m udp --sport 53 -j ACCEPT
sudo iptables -A INPUT -i wlp4s0 -p udp -m udp --sport 53 -j ACCEPT
sudo iptables -A OUTPUT -p udp -m udp --dport 53 -j ACCEPT
######################
#HTTP & HTTPS PORTS
sudo iptables -A INPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
######################
#HTTP & HTTPS PORTS
sudo iptables -A OUTPUT -p tcp -m tcp --sport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 80 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --sport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -p tcp -m tcp --dport 443 -m state --state NEW,ESTABLISHED -j ACCEPT
######################
#ICMP DROP
sudo iptables -A INPUT -p icmp -m icmp --icmp-type 17 -j DROP
sudo iptables -A INPUT -p icmp -m icmp --icmp-type 13 -j DROP
######################
#PORTSCAN LOG
sudo iptables -A INPUT -p tcp -m tcp --dport 139 -m recent --set --name PortScan --mask 255.255.255.0 --rsource -j LOG --log-prefix "PortScan !!!:"
sudo iptables -A FORWARD -p tcp -m tcp --dport 139 -m recent --set --name PortScan --mask 255.255.255.0 --rsource -j LOG --log-prefix "PortScan !!!:"
######################
#FTP SERVER CONNECTION
sudo iptables -A INPUT -s $MY_SERVER,$MY_HOSTING -p tcp --sport 21 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A INPUT -s $MY_SERVER,$MY_HOSTING -p tcp --sport 1024: --dport 1024: -m state --state ESTABLISHED,RELATED -j ACCEPT
sudo iptables -A INPUT -m state --state ESTABLISHED,RELATED -s $MY_SERVER,$MY_HOSTING,$MUTE_SERVER,$HOME -j ACCEPT
######################
#SSH PORTS 
sudo iptables -A INPUT -p tcp -s $MY_SERVER --sport 22222 -m state --state NEW -j ACCEPT
sudo iptables -A INPUT -p tcp -s $MUTE_SERVER,$HOME --sport 22 -m state --state NEW -j ACCEPT
######################
#SMB SERVER PORTS
sudo iptables -A INPUT -p udp -s $HOME --dport 137 -j ACCEPT
sudo iptables -A INPUT -p udp -s $HOME --dport 138 -j ACCEPT
sudo iptables -A INPUT -p tcp -s $HOME --dport 139 -j ACCEPT
sudo iptables -A INPUT -p tcp -s $HOME --dport 445 -j ACCEPT
######################
#FTP SERVER CONNECTION
sudo iptables -A OUTPUT -d $MY_SERVER,$MY_HOSTING -p tcp --dport 21 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -o wlp4s0 -p tcp --dport 21 -j ACCEPT
sudo iptables -A OUTPUT -o enp3s0 -p tcp --dport 21 -j ACCEPT
######################
#SSH PORTS
sudo iptables -A OUTPUT -o wlp4s0 -p tcp --dport 22 -j ACCEPT
sudo iptables -A OUTPUT -o enp3s0 -p tcp --dport 22 -j ACCEPT
sudo iptables -A OUTPUT -d $MUTE_SERVER,$HOME -p tcp --dport 22 -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $MY_SERVER -p tcp --dport 22222 -m state --state NEW,ESTABLISHED -j ACCEPT
######################
#FTP SERVER CONNECTION
sudo iptables -A OUTPUT -o enp3s0 -p tcp --dport 1024: -j ACCEPT
sudo iptables -A OUTPUT -o wlp4s0 -p tcp --sport 1024: -j ACCEPT
sudo iptables -A OUTPUT -d $MY_SERVER,$MY_HOSTING -p tcp --sport 1024: --dport 1024: -m state --state ESTABLISHED,RELATED -j ACCEPT
######################
#SMB SERVER PORTS
sudo iptables -A OUTPUT -d $HOME -p udp --sport 137:138 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $HOME -p tcp --sport 139 -m state --state ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $HOME -p tcp --sport 445 -m state --state ESTABLISHED -j ACCEPT
######################
#CUSTOM PORTS
sudo iptables -A OUTPUT -d $MY_SERVER -p tcp --dport $PORTS -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $MY_SERVER -p tcp --dport $PORTS -m state --state NEW,ESTABLISHED -j ACCEPT
sudo iptables -A OUTPUT -d $MY_SERVER -p tcp --dport $PORTS -m state --state NEW,ESTABLISHED -j ACCEPT
######################
#VIRTUAL TO ANOTHER HOST
#sudo iptables -A FORWARD -s $ANOTHER_HOST -i enp3s0 -o wboxnet0 -d $VIRTUAL -j ACCEPT
#sudo iptables -A FORWARD -s $ANOTHER_HOST -i enp3s0 -p wboxnet0 -d $VIRTUAL -m state --state #ESTABLISHED,RELATED -j ACCEPT
#sudo iptables -t nat -A POSTROUTING -o enp3s0 -j MASQUERADE 
######################
#SAVE & NOTIFY
sudo iptables-save
notify-send "Firewall" "Firewall is setted!" -i /usr/share/icons/Adwaita/32x32/status/changes-prevent.png & paplay /usr/share/sounds/KDE-Im-Internal-Error.ogg
