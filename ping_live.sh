host_file="targets.txt"
online_file="online.txt"
offline_file="offline.txt"
if [ -f "$online_file" ];
then
	rm "$online_file"
fi
	touch "$online_file"
if [ -f "$offline_file" ];
then
	rm "$offline_file"
fi
	touch "$offline_file"
cat "$host_file" | sort -u | while read line
do
   live=`ping -c 1 -t 2 "$line" 2>/dev/null | grep time | cut -d" " -f4 | cut -d":" -f1`
   if [ "$live" != "" ];
   then
       echo "$live - Accessible"
       echo "$line" >> "$online_file"
   else 
   		echo "$line - Inaccessible"
   		echo "$line" >> "$offline_file"
   fi
done