#!/bin/bash
# Emre Ovunc

files='192.168.*'
nameserver='8.8.8.8'
save='live_domains.txt'
touch $save
# tail is used for remove .emo local domain

for file_name in $files; do
    read_file=`cat $file_name|cut -f2`
    for domains in $read_file; do
        tail=`echo $domains|tail -c 4`
        if [[ $tail != *'emo'* ]]; then
            digger=`dig +short $domains @$nameserver`
            result=`echo $digger`
            if [[ $result != *'not known'* ]]; then
                domain=`echo $result|cut -d" " -f3`
                echo $domain "|" $domains|sort -u >> $save
            fi
        fi
    done
done
