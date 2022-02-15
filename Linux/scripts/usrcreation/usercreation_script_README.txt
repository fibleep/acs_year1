SCRIPT: USER CREATION SCRIPT FOR LINUX SERVER
TEAM: TEAM 3
CLASS: 101A
AUTHOR: FILIP NOWAK
2021-2022
--------------------------------------

sudo chown root.root /opt/usrcreation/usercreation.sh
sudo chmod u=rwx,g=r,o=r /opt/usrcreation/usercreation.sh

SCRIPT EXEC ACCESS ONLY FOR ROOT

This script will create users for every student included in ait_birthdays.csv
FORMATTING:

USERNAME: $name$dayofbirth
PASSWORD: $name$monthofbirth

EXAMPLE:

USERNAME:filip15
PASSWORD:filip06

The script will lock all created users that are not a part of TEAM 3
It will change the default shell to bash for everyone.

LOGFILE LOCATION: /var/opt/usrcreation/log.txt