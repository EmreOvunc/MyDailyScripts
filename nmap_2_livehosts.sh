#!/bin/bash
# EmreOvunc
dirs=`ls -l|awk '{print $9}'|sort -u`
for dir in $(echo $dirs); do
	cmd=`cat $dir/*.gnmap|egrep "Host|Up"|cut -d" " -f2|sort -u > $dir/live.txt`
done
