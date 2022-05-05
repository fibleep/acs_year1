#!/bin/bash
user='202122t13-ssh'

if [ ! -e  /home/$user/upload ]
then
mkdir /home/$user/upload
fi

if [ ! -e /home/$user/var/log ]
then
mkdir -p /home/$user/var/log
fi

latest=$(ls /home/$user/upload -lt | head -n2 | tail -n1)
toDelete=$(ls /home/$user/upload | wc -l)
filename=$(ls /home/$user/upload -t | head -1)
webPurge=$(ls /web)
# DELETING OLD GAME VERSIONS

if [ $toDelete -gt 1 ]
then
lof=$(ls /home/$user/upload  -t | tail -n+2)
for file in $lof
do
rm -rf /home/$user/upload/$file
done
# LOGGING THE SCRIPT
    echo -e "LATEST FILE: $filename\nDATE OF UPDATE: $(date)">/home/$user/var/log/scriptlog.txt
    echo -e "LAST UPDATE: $(date)\nLATEST FILE: $filename\n$(md5sum /home/$user/upload/$filename)\n $(sha512sum /home/$user/upload/$filename)\n$(sha256sum
/home/$user/upload/$filename)"
fi


# CLEANING PREVIOUS FOLDER

for file in $webPurge
do
if [[ "$file" != "legacy" ]]
then
rm -rf /web/$file
fi
done
rm -rf /web/$filename &>/dev/null
cp /home/$user/upload/$filename /web/$filename
cp /home/$user/var/log/hashcodes.txt /web/hashcodes.txt

# CLONING AND UNPACKING THE WEBSITE
pushd /web/legacy/stratego_web;git pull --rebase git@gitlab.com:fibleep/stratego_web;popd
cp -r /web/legacy/stratego_web/* /web

if [ $? ]
then
echo "\n git pull successful!" >> /home/$user/var/log/scriptlog.txt
fi