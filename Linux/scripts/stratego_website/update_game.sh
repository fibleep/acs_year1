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

lof=$(ls /home/$user/upload  -t | tail -n+2)
for file in $lof
do
rm -rf /home/$user/upload/$file
done
# LOGGING THE SCRIPT
    echo -e "LATEST FILE: $filename\nDATE OF UPDATE: $(date)\n">/home/$user/var/log/scriptlog.txt
    echo -e "LAST UPDATE: $(date)\n">/home/$user/var/log/hashcodes.txt
    echo -e "MD5: $(md5sum /home/$user/upload/$filename | cut -d' ' -f1)\n">>/home/$user/var/log/hashcodes.txt
    echo -e "SHA256: $(sha256sum /home/$user/upload/$filename | cut -d' ' -f1)\n">>/home/$user/var/log/hashcodes.txt
    echo -e "SHA512: $(sha512sum /home/$user/upload/$filename | cut -d' ' -f1)">>/home/$user/var/log/hashcodes.txt


# CLEANING PREVIOUS FOLDER

for file in $webPurge
do
if [[ "$file" != "legacy" ]] && [[ "$file" != ".htaccess" ]]
then
rm -rf /web/$file
if [ $? ]
then
echo -e "$file removed\n" >> /home/$user/var/log/scriptlog.txt
fi
fi
done
rm -rf /web/$filename &>/dev/null
cp /home/$user/upload/$filename /web/stratego.jar
cp /home/$user/var/log/hashcodes.txt /web/hashcodes.txt

# CLONING AND UNPACKING THE WEBSITE
pushd /web/legacy/stratego_web;git pull --rebase git@gitlab.com:fibleep/stratego_web 2>>/home/$user/var/log/scriptlog.txt;popd
cp -r /web/legacy/stratego_web/* /web

if [ $? ]
then
echo -e "\n files copied successfully!" >> /home/$user/var/log/scriptlog.txt
fi