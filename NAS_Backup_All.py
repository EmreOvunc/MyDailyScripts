#!/usr/bin/python

import os

def main():
    os.system("notify-send 'Backup' 'NAS Backup Starting...' -i /usr/share/pixmaps/xarchiver/xarchiver-extract.png ")
    os.system("sudo mount -o username='emre' //192.168.1.2/Samba /media/NAS")
    os.system("sudo rsync -av --include='.profile' --include='.bash*' --exclude='.*' --exclude='VirtualBox*' --exclude='BurpSuite*' --delete /home/monster /media/NAS")
    os.system("sudo umount /media/NAS")
    os.system("python /home/monster/Scripts/emre-mailclient-weeklybackup.py")
    os.system("notify-send 'Backup' 'NAS Backup Completed!' -i /usr/share/pixmaps/xarchiver/xarchiver-add.png & paplay /usr/share/sounds/KDE-Im-User-Auth.ogg")

main()
