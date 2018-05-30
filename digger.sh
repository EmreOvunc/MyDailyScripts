#!/bin/bash
# Emre Ovunc

files='192.168.*'
nameserver='8.8.8.8'
# tail is used for removing .emo local domain

for file_name in $files; do
    read_file=`cat $file_name|cut -f2`
    for domains in $read_file; do
        tail=`echo $domains|tail -c 4`
        if [[ $tail != *'emo'* ]]; then
            digger=`dig +short $domains @$nameserver`
            result=`echo $digger`
            if [[ $result != *'not known'* ]]; then
                domain=`echo $result|cut -d" " -f3`
                echo $domain "|" $domains|sort -u > live_domains.txt
            fi
        fi
    done
done
