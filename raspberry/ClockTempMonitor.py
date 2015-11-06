#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime

import socket
import fcntl
import struct
import os
import glob

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'

lcd = Adafruit_CharLCD()
lcd.begin(16, 1)

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return str(round(temp_c,2)), str(round(temp_f,2))

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

flag = False
while 1:
    lcd.clear()
    lcd.message(datetime.now().strftime('%b %d  %H:%M %p\n'))
    
    if flag:
        lcd.message('IP %s' % get_ip_address('wlan0'))
        flag = False
    else:
        temp = read_temp()
        lcd.message('  Temp: %sC' % (temp[0]+ chr(223)))
        #print(read_temp())
        flag = True
    
    sleep(20)
