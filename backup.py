#!/usr/bin/python
import os

def main():
    os.system("notify-send 'Backup' 'Hourly Backup Starting...' -i /usr/share/pixmaps/xarchiver/xarchiver-extract.png")
    os.system("mount /dev/sdc5")
    os.system("rsync -av --delete /home/monster/Desktop /media/backup/Debian/monster")
    os.system("umount /dev/sdc5")
    os.system("python /home/monster/Scripts/emre-mailclient-backup.py")
    os.system("notify-send 'Backup' 'Hourly Backup Completed!' -i /usr/share/pixmaps/xarchiver/xarchiver-add.png & paplay /usr/share/sounds/KDE-Im-User-Auth.ogg")

main()
