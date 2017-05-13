#!/usr/bin/python
import os

def main():
    os.system("notify-send 'Backup' 'Weekly Backup Starting...' -i /usr/share/pixmaps/xarchiver/xarchiver-extract.png ")
    os.system("mount /dev/sdc6")
    os.system("rsync -av --include='.profile' --include='.bash*' --exclude='.*' --exclude='Downloads' --exclude='VirtualBox*' --exclude='BurpSuite*' --exclude='Videos' --delete /home/monster/ /media/backup/")
    os.system("sudo umount /dev/sdc6")
    os.system("python /home/monster/Scripts/emre-mailclient-weeklybackup.py")
    os.system("notify-send 'Backup' 'Weekly Backup Completed!' -i /usr/share/pixmaps/xarchiver/xarchiver-add.png & paplay /usr/share/sounds/KDE-Im-User-Auth.ogg")

main()
