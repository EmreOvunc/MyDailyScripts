#!/bin/bash
for host in $(cat taranmayan.txt); do x1=`echo $host|cut -d"-" -f1`; x2=`echo $host|cut -d"-" -f2`; x3=`echo $host|cut -d"-" -f3`; x4=`echo $host|cut -d"-" -f4`; x5=`echo $host|cut -d"-" -f5`; ip=`echo $x1.$x2.$x3.$x4/$x5`; outf=`echo $x1-$x2-$x3-$x4-$x5`; mkdir live_kalanlar/$outf; nmap -sn -n $ip -oA live_kalanlar/$outf/$outf; done
