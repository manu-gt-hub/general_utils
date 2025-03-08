#!/bin/bash

# ***** INFORMATION *****
# Usage
# yes | ./environment.sh

# to remove any package:
# sudo sudo apt-get install [PACKAGE_NAME]

# check favourite apps array
# gsettings get org.gnome.shell favorite-apps

BLACK="\033[30m"
RED="\033[31m"
GREEN="\033[32m"
YELLOW="\033[33m"
BLUE="\033[34m"
PINK="\033[35m"
CYAN="\033[36m"
WHITE="\033[37m"
NORMAL="\033[0;39m"

# UPDATE EVERYTHING
sudo -E apt-get update
sudo snap refresh

# INSTALL SUBLIME
printf "\n ${RED} ---> instalando SUBLIME... ${NORMAL} \n\n"
sudo snap install sublime-text --classic

# INSTALL CHROMIUM
printf "\n ${RED} ---> instalando CHROMIUM... ${NORMAL} \n\n"
sudo -E apt-get install chromium-browser

# INSTALL TERMINATOR
printf "\n ${RED} ---> instalando TERMINATOR... ${NORMAL} \n\n"
sudo -E apt-get install terminator

# INSTALL SLACK
printf "\n ${RED} ---> instalando SLACK... ${NORMAL} \n\n"
sudo snap install slack --classic

# INSTALL INTELLIJ
printf "\n ${RED} ---> instalando INTELLIJ... ${NORMAL} \n\n"
sudo snap install intellij-idea-community --classic

#INSTALL KEE PASS
printf "\n ${RED} ---> instalando KEE PASS... ${NORMAL} \n\n"
sudo -E apt-get install keepass2

# INSTALL CURL
printf "\n ${RED} ---> instalando CURL... ${NORMAL} \n\n"
sudo apt install curl

# INSTALL GIT
printf "\n ${RED} ---> instalando GIT... ${NORMAL} \n\n"
sudo -E apt install git-all

# INSTALL VIM
printf "\n ${RED} ---> instalando VIM... ${NORMAL} \n\n"
sudo -E apt install vim

# INSTALL KAZAM
printf "\n ${RED} ---> instalando KAZAM... ${NORMAL} \n\n"
sudo -E apt install kazam

# INSTALL GITKRAKEN
printf "\n ${RED} ---> instalando GITKRAKEN... ${NORMAL} \n\n"
sudo snap install gitkraken --classic

# INSTALL POSTMAN
printf "\n ${RED} ---> instalando POSTMAN... ${NORMAL} \n\n"
sudo snap install postman --classic


# UPDATE EVERYTHING
printf "\n ${YELLOW} ---> ACTUALIZANDO... ${NORMAL} \n\n"
sudo snap refresh
sudo -E apt-get update

# CHECK INSTALLATION
printf printf $GREEN
printf "\n ${GREEN} ---> CHECKING INSTALLATION... ${NORMAL}\n\n"
printf "\n ---> SUBLIME version: ${NORMAL}\n"
subl --version
printf "\n ${GREEN} ---> CHROMIUM version: ${NORMAL}\n"
chromium-browser --version
printf "\n ${GREEN} ---> TERMINATOR version: ${NORMAL}\n"
terminator --version
printf "\n ${GREEN} ---> SLACK version: ${NORMAL}\n"
snap info slack
printf "\n ${GREEN} ---> INTELLIJ version: ${NORMAL}\n"
snap info intellij-idea-community
printf "\n ${GREEN} ---> KEE PASS version: ${NORMAL}\n"
keepass2 --version
printf "\n ${GREEN} ---> CURL version: ${NORMAL}\n"
curl --version
printf "\n ${GREEN} ---> GIT version: ${NORMAL}\n"
git --version
printf "\n ${GREEN} ---> VIM version: ${NORMAL}\n"
vim --version
printf "\n ${GREEN} ---> KAZAM version: ${NORMAL}\n"
kazam -v
printf "\n ${GREEN} ---> GIT KRAKEN version: ${NORMAL}\n"
gitkraken -v

# SETTING APPS TO FAVOURITES
printf printf $GREEN
printf "\n ${GREEN} ---> SETTING APPS TO FAVOURITES... ${NORMAL}\n\n"
gsettings set org.gnome.shell favorite-apps "$(gsettings get org.gnome.shell favorite-apps | sed s/.$//), 'chromium-browser.desktop', 'slack_slack.desktop', 'intellij-idea-community_intellij-idea-community.desktop', 'org.gnome.Nautilus.desktop', 'terminator.desktop', 'kazam.desktop', 'org.gnome.Screenshot.desktop', 'sublime-text_subl.desktop', 'postman_postman.desktop', 'keepass2.desktop', 'gnome-calculator_gnome-calculator.desktop', 'gnome-system-monitor_gnome-system-monitor.desktop', 'org.gnome.Software.desktop', 'gnome-control-center.desktop']"

# SETTING BOOKMARKS
printf printf $GREEN
printf "\n ${GREEN} ---> SETTING BOOKMARKS... ${NORMAL}\n\n"
rm $HOME/.config/chromium/Default/Bookmarks
cp ./files/Bookmarks $HOME/.config/chromium/Default/Bookmarks

