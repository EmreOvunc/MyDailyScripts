#!/bin/bash
# EmreOvunc

#whitelist.txt contains;
#192.168.1.x
#172.16.150.x

#ipler.txt contains;
#192.168.2.1, 10.0.0.1, 172.16.24.10

file_name='whitelist.txt'
read_file=`cat $file_name`

sick_file='ipler.txt'
read_sick=`cat $sick_file`

all=''

for line in $read_sick ; do
    ip_check=`echo $line`
    if [[ $ip_check = *','* ]]; then
        ip=`echo $ip_check|sed s'/.$//'`
    else
        ip=`echo $ip_check`
    fi
    ip_=`echo $ip|cut -d":" -f1`
    if [ ! "$ip_" ]; then
        break
    fi
    for l1ne in $read_file ; do
        white_ip=`echo $l1ne|cut -d"." -f1,2,3|sed 's/$/./g'`
	if [[ $ip_ = *"$white_ip"* ]]; then
            all+=`echo "$ip, "`
            echo "$ip - $white_ip"
        fi
    done
done
echo $all|xclip -sel clipboard
