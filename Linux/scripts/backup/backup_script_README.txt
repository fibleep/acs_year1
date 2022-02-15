SCRIPT: BACKUP SCRIPT FOR LINUX SERVER
TEAM: TEAM 3
CLASS: 101A
AUTHOR: FILIP NOWAK
2021-2022
--------------------------------------
sudo nano /etc/crontab

CHANGE TO 
0 1	* * *  root  /opt/backup/backup.sh

sudo chown root.root /opt/backup/backup.sh
sudo chmod u=rwx,g=r,o=r /opt/backup/backup.sh

SCRIPT EXEC ACCESS ONLY FOR ROOT.

This script will backup all of the files and folders mentioned in /opt/backup/backuplist.txt
There's a check implemented to test if path exists.
crontab is set to backup everything at 00:01 everyday

LOGFILES are stored in /var/opt/backup

-backup.txt gives a short rundown of every filed backed up, the contents are saved throughout multiple days:
-- FORMAT:
-- DD-MM-YYYY
When folder exists
-- $folder backed up 
When folder not found
-- unable to backup $folder

-exec.txt saves the daily verbose output of tar command

