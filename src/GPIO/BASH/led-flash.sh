#!/bin/bash
sudo echo 17 > /sys/class/gpio/export
sudo echo out > /sys/class/gpio/gpio17/direction
# loop forever
while true
do
  sudo echo 1 > /sys/class/gpio/gpio17/value
  sleep 0.5
  sudo echo 0 > /sys/class/gpio/gpio17/value
  sleep 0.5
done

# Don't forget to remove the GPIO pin from file access by using the following command:
# $ sudo echo 17 > /sys/class/gpio/unexport