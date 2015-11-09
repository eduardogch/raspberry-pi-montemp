# Raspberry Pi Clock and Temperature Monitor
Project Raspberry Pi for a clock and monitor temperature with a LCD 16x2

`Version: 1.5.0 Stable`

-----

## Requirements

* Ubuntu, Mac, Windows
* Raspberry Pi 1 Model B
* Python, HTML, CSS
* LCD 16x2

## Video
[![IMAGE ALT TEXT HERE](http://img.youtube.com/vi/mBpfsGmuFqE/0.jpg)](http://www.youtube.com/watch?v=mBpfsGmuFqE)

-----

# Quick Install
Just run in the console this commands in the Raspberry Pi:

	sudo easy_install -U distribute
	sudo apt-get install python-pip
	sudo pip install rpi.gpio
	wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz
	tar xvzf WebIOPi-0.7.1.tar.gz
	cd WebIOPi-0.7.1
	sudo ./setup.sh
	sudo webiopi-passwd
	sudo /etc/init.d/webiopi start
	sudo update-rc.d webiopi defaults

# Circuits

How to conect Raspberry Pi to LCD 16x2

![alt tag](https://raw.githubusercontent.com/eduardogch/raspberry-pi-montemp/master/circuits/circuit.png)

How to conect Raspberry Pi to Temperature Sendor
![alt tag](https://raw.githubusercontent.com/eduardogch/raspberry-pi-montemp/master/circuits/DS18B20-rpi-setup-3.JPG)

Raspberry Pi GPIO's

![alt tag](https://raw.githubusercontent.com/eduardogch/raspberry-pi-montemp/master/circuits/raspberry-pi-rev2-gpio-pinout.jpg)

-----

### Fix broke the WebIOPi 1-wire code
	sudo nano /boot/config.txt
	# Fix w1-gpio
	dtoverlay=w1-gpio-pullup,gpiopin=4

### Copy scripts in Raspberry Pi

	mkdir clock-temp-monitor
	cd clock-temp-monitor
	# Copy files from the raspberry github Repository folder in the folder clock-temp-monitor
	sudo chmod +x *

### Start-up script in Raspberry Pi

	sudo nano /etc/init.d/ClockTempMonitor
	# Copy and paste in the console the file ClockTempMonitor
	sudo chmod 755 /etc/init.d/ClockTempMonitor
	sudo update-rc.d ClockTempMonitor defaults

-----

## Additional Information

Email [Email](mailto:eduardo.gch@gmail.com)

Twitter [Twitter](https://twitter.com/eduardochavira_)

GitHub [GitHub](https://github.com/eduardogch/raspberry-pi-montemp)

Issues [Issues](https://github.com/eduardogch/raspberry-pi-montemp/issues)
