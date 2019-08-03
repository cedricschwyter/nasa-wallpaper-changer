#!/usr/bin/env python3

import os
import subprocess
import urllib.request as url
from bs4 import BeautifulSoup


ROOT_URL = "https://apod.nasa.gov/apod/"
IMG_DIR = "/usr/local/src/nasa-image/"
IMG_STUB = "nasa-iotd.jpg"


def get_nasa_iotd_site():

    print("Connecting to NASA's Astronomy Picture Of The Day page...")
    file = url.urlopen(ROOT_URL + "astropix.html")
    print("Successfully connected to NASA's Astronomy Picture Of The Day page")
    site = file.read().decode('UTF-8')
    print("Successfully decoded NASA's Astronomy Picture Of The Day page")
    file.close()
    print("Closing connection...")

    return site


def extract_iotd_from_nasa_iotd_site():

    site = get_nasa_iotd_site()
    print("Parsing site...")
    parser = BeautifulSoup(site, "html.parser")
    img = parser.find('img')

    return img['src']


def set_gnome_wallpaper(file_path_):

    command = "gconftool-2 --set \
            /desktop/gnome/background/picture_filename \
            --type string '%s'" % file_path_
    status, output = subprocess.getstatusoutput(command)

    return status


def main():

    print("Starting nasa-wallpaper-changer service...")
    image = extract_iotd_from_nasa_iotd_site()
    image_url = ROOT_URL + image
    print("Image URL: " + image_url)
    image_data = url.urlopen(image_url).read()

    try:

        os.mkdir(IMG_DIR)

    except FileExistsError:

        pass

    try:

        image_disk = open(IMG_DIR + IMG_STUB, "bw+")
        image_disk.write(image_data)
        image_disk.close()
        print("Successfully written to destination directory")
        print("Attempting to set as background...")
        if not set_gnome_wallpaper(IMG_DIR + IMG_STUB):

            print("Successfully set as background")

        else:

            print("Failed to set as background")

    except OSError:

        print("Failed to create directory " + IMG_DIR + ", try run as superuser.")


if __name__ == "__main__":

    main()
