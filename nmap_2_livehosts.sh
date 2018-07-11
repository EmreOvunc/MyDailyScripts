#!/bin/bash
# EmreOvunc
dirs=`ls -la|awk '{print $9}'|sort -u`
for dir in $(echo $dirs); do
	cmd=`cat $dir/*.gnmap|egrep "Host|Up"|cut -d" " -f2|sort -u > $dizin/live.txt`
done
