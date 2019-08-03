#!/usr/bin/env bash

echo "Installing nasa-wallpaper-changer..."
cp -R nasa-wallpaper-changer/ /usr/local/bin/nasa-wallpaper-changer
echo "Installing new crontab..."
crontab -l > mycron
echo "@reboot python3 -m /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer" >> mycron
crontab mycron
rm mycron
echo "Successfully installed new crontab"
echo "Successfully installed nasa-wallpaper-changer"
