# Raspberry Pi Clock and Temperature Monitor
Project Raspberry Pi for a clock and monitor temperature with a LCD 16x2

`Version: 1.0.0 Stable`

-----

## Requirements

* Ubuntu, Mac, Windows
* Raspberry Pi, 
* Python, HTML, CSS
* LCD 16x2

## Project base on:

	http://www.rototron.info/projects/pi-temperature-monitor/

-----

# Quick Install in Raspberry Pi
Just run in the console this commands:

	wget http://sourceforge.net/projects/webiopi/files/WebIOPi-0.7.1.tar.gz
	tar xvzf WebIOPi-0.7.1.tar.gz
	cd WebIOPi-0.7.1
	sudo ./setup.sh
	sudo webiopi-passwd
	sudo /etc/init.d/webiopi start
	sudo update-rc.d webiopi defaults

### Fix broke the WebIOPi 1-wire code
	sudo nano /boot/config.txt
	# Fix w1-gpio
	dtoverlay=w1-gpio-pullup,gpiopin=4

### Copy scripts and html files in raspberry

	mkdir clock-temp-monitor
	cd clock-temp-monitor
	wget https://github.com/eduardogch/raspberry-pi-montemp/blob/master/raspberry/index01.html
	wget https://github.com/eduardogch/raspberry-pi-montemp/blob/master/raspberry/lcd.py
	wget https://github.com/eduardogch/raspberry-pi-montemp/blob/master/raspberry/script01.py
	sudo chmod +x *

-----

## Additional Information

Email [Email](mailto:eduardo.gch@gmail.com)

Twitter [Twitter](https://twitter.com/eduardochavira_)

GitHub [GitHub](https://github.com/eduardogch/raspberry-pi-montemp)

Issues [Issues](https://github.com/eduardogch/raspberry-pi-montemp/issues)
