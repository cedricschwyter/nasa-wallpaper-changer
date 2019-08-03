#!/usr/bin/env bash

echo "Installing dependencies..."
pip3 install bs4
echo "Successfully installed dependencies"
echo "Installing nasa-wallpaper-changer..."
cp -R nasa-wallpaper-changer/ /usr/local/bin/nasa-wallpaper-changer
echo "Installing new crontab..."
crontab -l > mycron
echo "@reboot python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py" >> mycron
echo "@hourly python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py" >> mycron
echo "0 0 * * * python3 /usr/local/bin/nasa-wallpaper-changer/nasa-wallpaper-changer.py" >> mycron
crontab mycron
rm mycron
echo "Successfully installed new crontab"
echo "Successfully installed nasa-wallpaper-changer"
echo "This tool will run every hour in the background and check if a new image is available"
