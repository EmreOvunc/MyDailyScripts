#!/bin/bash
live_hosts=$1
scan=`nbtscan -f $live_hosts > netbios_scan.txt`
for host in $(cat netbios_scan.txt|grep server|cut -d" " -f1); do
	echo "############"
        echo $host
	rpcclient -U "" $host
	echo "############"
done

