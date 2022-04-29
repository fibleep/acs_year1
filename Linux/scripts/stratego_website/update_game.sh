#!/bin/bash
IFS='
'
if [ ! -e  /media/game ]
then
mkdir /media/game
fi
lof = $(ls /media/game)
toDelete = $(ls /media/game | wc -l)
if [! -e /var/log ]
then
mkdir -p /var/log
fi
if [ ! -e /var/log/hash_codes.txt ]
then
touch /var/log/hash_codes.txt
fi
if [ toDelete -eq 2 ]
then
   
else
for file in $lof
    do
    md5sum $file >> /var/log/hash_codes.txt
    echo -e "\n" > /var/log/hash_codes.txt
    sha512sum $file > /var/log/hash_codes.txt
    echo -e "\n" > /var/log/hash_codes.txt
    sha256sum $file> /var/log/hash_codes.txt
    done
fi