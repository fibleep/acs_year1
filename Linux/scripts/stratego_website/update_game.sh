#!/bin/bash
IFS='
'
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
filename=$(ls /home/$user/upload -lt | head -n2 | tail -n1 | cut -d' ' -f10)
webPurge=$(ls /web)

# CLEANING PREVIOUS FOLDER

for file in $webPurge
do
if [[ "$file" != "legacy" ]]
then
rm -rf /web/$file
fi
done

# CLONING AND UNPACKING THE WEBSITE
pushd /web/legacy/stratego_web;git pull git@gitlab.com:fibleep/stratego_web;popd
mv /web/legacy/stratego_web/* /web

# DELETING OLD GAME VERSIONS
if [ $toDelete -gt 1 ]
then
lof=$(ls /home/$user/upload  -t | tail -n+2)
for file in $lof
do
rm /home/$user/upload/$file
done
# LOGGING THE SCRIPT
    echo -e "LATEST FILE: $filename\nDATE OF UPDATE: $(date)">/home/$user/var/log/scriptlog.txt
    echo -e "LAST UPDATE: $(date)\nLATEST FILE: $filename\n md5: $(md5sum /home/$user/upload/$filename| cut -d' ' -f1)\n sha512:$(sha512sum /home/$user/upload/$filename | cut -d' ' -f1)\n sha256:$(sha256sum /home/$user/upload/$filename | cut -d' ' -f1)" > /home/$user/var/log/hashcodes.txt
fi