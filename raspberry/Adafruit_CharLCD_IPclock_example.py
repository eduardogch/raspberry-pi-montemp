#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

import socket
import fcntl
import struct

lcd = Adafruit_CharLCD()

lcd.begin(16, 1)


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%b %d  %H:%M %p\n'))
    lcd.message('IP %s' % get_ip_address('wlan0'))
    sleep(60)
