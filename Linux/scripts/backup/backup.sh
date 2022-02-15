#!/bin/bash
IFS='
'
#variables
logfile=/var/opt/backup/backup.txt
execfile=/var/opt/backup/exec.txt
backuplist=$(cat /opt/backup/backuplist.txt)
currentdate=$(date +%d-%m-%Y)
if [ ! -e /media/backup ] #does backups folder exist?
then
mkdir /media/backup #if not, create backups
fi
if [ ! -e /var/opt/backup ] #does backup exist? (folder for storing logs)
then
mkdir /var/opt/backup #if not, create backup
fi
rm $execfile
find /media/backup/* -mtime +6 -exec rm {} \;  #delete backups which are 7>= days old
echo $currentdate >> $logfile #formatting logfile
for folder in $backuplist #iterate through every path saved in backuplist
do
tar rvf /media/backup/backup-$currentdate.tar $folder &>$execfile #append every folder in backuplist to archive, output is saved in execfile
 if [ -e $folder ] #checks if exists, which is a condition for folder/file to be backed up
 then
 echo $folder backed up >> $logfile
 else [ ! -e $folder ] 
 echo unable to backup $folder >> $logfile
fi
done
gzip -f /media/backup/backup-$currentdate.tar
