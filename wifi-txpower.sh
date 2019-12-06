#!/bin/sh
sudo ifup wlan1
sudo ifconfig wlan1 down
sudo iw reg set US
sudo iwconfig wlan1 txpower 27
sudo ifconfig wlan1 up
sudo iwconfig

'''
apt-get install python-m2crypto libgcrypt11-dev libnl-3-dev libnl-genl-3-dev
curl -sSL https://www.kernel.org/pub/software/network/crda/crda-3.18.tar.xz | tar xJf -
curl -sSL https://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-2016.06.10.tar.xz | tar xJf -
cd wireless-regdb-2016.06.10
sed -i '/country CN/{n;s/20/30/}' db.txt
make
mv /lib/crda/regulatory.bin /lib/crda/regulatory.bin.old
cp regulatory.bin /lib/crda/
chmod +x /lib/crda/regulatory.bin
cp root.key.pub.pem ../crda-3.18/pubkeys/
cp /lib/crda/pubkeys/*.pem ../crda-3.18/pubkeys/
cd ../crda-3.18
sed -i 's/\/usr//' Makefile
sed -i 's/-Werror//' Makefile
make
make install
reboot
'''