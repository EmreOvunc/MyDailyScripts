#!/usr/bin/python
import os
def main():
    os.system("notify-send 'Backup Compress' 'Backup Compress Starting...'-i /usr/share/pixmaps/xarchiver/xarchiver-extract.png ")
    os.system("mount /dev/sdc5")
    os.system("tar -cvjf /media/backup/Weekly_$(date +%Y%m%d).tar.bz2 /media/backup/Debian/monster")
    os.system("umount /dev/sdc5")
    os.system("python /home/monster/Scripts/emre-mailclient-weeklytar.py")
    os.system("notify-send 'Backup Compress' 'Backup Compress Completed!' -i /usr/share/pixmaps/xarchiver/xarchiver-add.png & paplay /usr/share/sounds/KDE-Im-User-Auth.ogg")

main()


