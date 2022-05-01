#!/bin/bash
IFS='
'
if [ ! -e  /media/game ]
then
mkdir /media/game
fi
latest = $(ls /media/game -lt | head -n2 | tail -n1)

toDelete = $(ls /media/game | wc -l)
if [! -e /var/log ]
then
mkdir -p /var/log
fi
if [ toDelete -gt 3 ]
then
lof = $(ls /media/game -t | tail -n+4) # keeps last 3 versions
for file in $lof
 rm /media/game/$file
do
done
else
    file = $(ls /media/game -lt | head -n2 | tail -n1 | cut -d" "-f9)
    echo -e "LATEST FILE: $file\nDATE OF UPDATE: $(date)">>var/log/scriptlog.txt
    echo -e "LATEST FILE: $file\n md5: $(md5sum $file)\n sha512:$(sha512sum $file)\n sha256:$(sha256sum $file)" >> /var/log/hash_codes.txt
fi