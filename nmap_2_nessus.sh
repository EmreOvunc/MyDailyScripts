#!/bin/bash
#EmreOvunc
# Change localhost:8834 to your nessus | x4 times
# Change X-API-Token | x2 times
# Change uuid | x1 times
# Change username and password | x1 times
login=`curl -i -s -k  -X $'POST' \
    -H $'Host: localhost:8834' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://localhost:8834/' -H $'Content-Type: application/json' -H $'X-API-Token: XXXXXX-XXXXX-XXXXX-XXXXXX' -H $'Connection: close' \
    --data-binary $'{\"username\":\"emre\",\"password\":\"Passw0rd\"}' \
    $'https://localhost:8834/session'`
tokenim=`echo $login|cut -d":" -f15|cut -d"}" -f1| sed 's:^.\(.*\).$:\1:'`
dir=`ls -l|awk '{print $9}'|sort -u`
rm -rf dizin.txt 2</dev/null
touch dizin.txt
for dizin in $(echo $dir); do
	dirornot=`file $dizin|awk '{print $2}'`
	if [[ $dirornot == 'directory' ]]; then
		cmd=`cat $dizin/*.gnmap|egrep "Host|Up"|cut -d" " -f2|sort -u > $dizin/live.txt`
		read_live=`cat $dizin/live.txt`
		lives=`echo $read_live|tr " " ','`
		rm -rf req.txt 2</dev/null
		echo -e '{"uuid":"xxxxx-xxxxx-xxxx-xxxxxxxxx","settings":{"attach_report":"no","emails":"","filter_type":"and","filters":[],"launch_now":false,"enabled":false,"file_targets":"","text_targets":"'$lives'","policy_id":"XXXX","scanner_id":"1","folder_id":3,"description":"AutoAdded_Scan","name":"'$dizin'"}}' > req.txt
		add_nessus=`curl -X POST -H "Content-Type: application/json; charset=utf-8" -H "X-Cookie: token=$tokenim" -H "X-API-Token: XXXXXX-XXXXX-XXXXX-XXXXXX" -d@req.txt https://localhost:8834/scans -k`
		echo $add_nessus
	fi
done
