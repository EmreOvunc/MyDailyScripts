#!/bin/bash
filename=`cat subdomains.txt`
for host in $filename;
do
    IP=`dig $host |grep $host |grep -v ';' |awk '{ print $5 }' |grep -v 'A'`
    echo $host - $IP
done