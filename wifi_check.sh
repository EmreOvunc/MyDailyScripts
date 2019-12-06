#!/bin/bash

interface="wlp3s0"
wlan_check=`ifconfig $interface | grep inet\ addr | cut -d":" -f2 | cut -d" " -f1`

if [[ $wlan_check =~ ^([0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}) ]]; then
	exit
else
	/sbin/ifdown $interface && /sbin/ifup $interface
fi
