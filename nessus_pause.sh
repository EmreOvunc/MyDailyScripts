#!/bin/bash
#EmreOvunc
login=`curl -i -s -k  -X $'POST' \
    -H $'Host: localhost:8834' -H $'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0' -H $'Accept: */*' -H $'Accept-Language: en-US,en;q=0.5' -H $'Accept-Encoding: gzip, deflate' -H $'Referer: https://localhost:8834/' -H $'Content-Type: application/json' -H $'X-API-Token: XXXXXX-XXXX-XXXX-XXXXXX' -H $'Connection: close' \
    --data-binary $'{\"username\":\"emre\",\"password\":\"Passw0rd\"}' \
    $'https://localhost:8834/session'`
tokenim=`echo $login|cut -d":" -f15|cut -d"}" -f1| sed 's:^.\(.*\).$:\1:'`
pause_nessus=`curl -X POST -H "Content-Type: application/json; charset=utf-8" -H "X-Cookie: token=$tokenim" -H "X-API-Token: XXXXX-XXXX-XXXX-XXXXX-XXXXXXX" https://localhost:8834/scans/XXX/pause -k`
echo $pause_nessus
