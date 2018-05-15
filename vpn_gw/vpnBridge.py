import os
import subprocess
firefox_Proc = subprocess.Popen(['ifconfig | grep tun'], stdout=subprocess.PIPE, shell=True) 
(out, err) = firefox_Proc.communicate()
if out.decode() != "":
    pass
else:
    os.system('sudo pkill -9 openvpn')
    os.system('bash /home/pi/openvpn.sh')
