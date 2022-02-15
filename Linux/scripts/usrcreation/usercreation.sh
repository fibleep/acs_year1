#!/bin/bash
file=$(cat /opt/usrcreation/ait1_birthdays.csv)
IFS='
'
if [ ! -e /var/opt/usrcreation ]
then
mkdir /var/opt/usrcreation #create folder for log storing
fi
if [ $(id -u) -eq 0 ] #check if root
then
for line in $file
do
workspace=$(echo $line | iconv -f utf-8 -t ascii//TRANSLIT ) #iconv was used to change a special character into a UTF-8 character
name=$(echo $workspace | cut -d"," -f2 | tr [:upper:] [:lower:] | tr -d "-" | tr -d " ") #translate name to lowercase with no spaces
dob=$(echo $workspace | cut -d"," -f3 | cut -d"." -f1)
mob=$(echo $workspace | cut -d"," -f3 | cut -d"." -f2)
username=$(echo $name$dob) #name format example: filip15 
password=$(echo $name$mob) #passwd format example: filip06
testcon=$(id -u $username)
if [ ! $testcon ]  #check if user is not yet created
then
useradd -m -d /home/$username $username #create user with home directory + /etc/skel contents
echo $username:$password | chpasswd #change password
addgroup $username sudo #add user to sudo
mkdir /home/$username/Upload #create folder Upload
chown -R $username.$username /home/$username #change perms 
usermod -s /bin/bash $username #change default shell to bash
echo User $username created succesfully! Congrats! >> /var/opt/usrcreation/log.txt
fi
if [ $username == "hasan24" ] || [ $username == "noah21" ] || [ $username == "sneha08" ] || [ $username == "filip15" ] || [ $username == "brandon05" ] #check if user is a part of the team 3
then
echo i hope we get a good grade for this !!!! > /dev/null # :^)
else
passwd -l $username > /dev/null #locks user if not a part of team3
echo User $username locked succesfully >> /var/opt/usrcreation/log.txt
fi
done
else
echo RUN AS ROOT
fi
