#!/bin/bash

cat << EOF
Sound must be disabled to use GPIO18.
This can be done in /boot/config.txt by changing "dtparam=audio=on" to "dtparam=audio=off" and rebooting.
Failing to do so can result in a segmentation fault.
EOF

sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
sudo python3 -m pip install --force-reinstall adafruit-blinka
