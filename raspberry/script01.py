# -*- coding: utf-8 -*-

# Author : rdagger
# Site   : http://www.rototron.info
# 
# Date   : 19/08/2013

# Imports
import time
import sys
sys.path.append("/home/pi/webiopi/test01/scripts")
import webiopi
import lcd

# Initialize LCD display
lcd.__init__()

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

# Temperature cold/hot thresholds
COLD = 69.0
HOT = 79.0

# RGB LED GPIO pins
RED = 11
GREEN = 9
BLUE = 10

# Switch GPIO
# Next version of WebIOPi should support interrupts (better approach)
SWITCH = 18

# Display State: Current Temperature or Temperature Range
displayCurrent = False

# Set temperature sensor (specified in WebIOPi config)
t = webiopi.deviceInstance("ServerRoom")

# Initialize temperature range variables
tLow = t.getFahrenheit()
tHigh = t.getFahrenheit()

# WH1602B-CTI Colors at 3.3V
Colors = {'Red':         (0.0,1.0,1.0),
          'Green':       (1.0,0.0,1.0),
          'Blue':        (1.0,1.0,0.0),
          'Purple':      (0.0,1.0,0.0),
          'Chartreuse':  (0.0,0.0,1.0),
          'Cyan':        (1.0,0.0,0.0),
          'Aquamarine':  (1.0,0.0,0.5),
          'Turquoise':   (1.0,0.5,0.0),
          'Violet':      (0.0,1.0,0.5),
          'Slate Blue':  (0.5,1.0,0.0),
          'Lime':        (0.5,0.0,1.0),
          'Yellow Green':(0.0,0.5,1.0),
          'Peach':       (0.0,0.9,1.0),
          'Orange':      (0.0,0.96,1.0),
          'Yellow':      (0.0,0.7,1.0),
          'White':       (0.0,0.6,0.8)} 
 
# Sets LCD display text color
def setColor(rgb):
    GPIO.pwmWrite(RED, rgb[0])
    GPIO.pwmWrite(GREEN, rgb[1])
    GPIO.pwmWrite(BLUE, rgb[2])


# Called by WebIOPi when service starts
def setup():
    webiopi.debug("Script with macros - Setup")
    # Setup GPIOs
    GPIO.setFunction(RED, GPIO.PWM)
    GPIO.setFunction(GREEN, GPIO.PWM)
    GPIO.setFunction(BLUE, GPIO.PWM)
    GPIO.setup(SWITCH, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

# Looped by WebIOPi
def loop():
    # Run every 5 seconds
    try:
        # Get current temperature
        fahrenheit = t.getFahrenheit()
        webiopi.debug("Current: %0.1f°F" % fahrenheit)

        # Set high & low
        global tHigh
        global tLow
        if fahrenheit > tHigh:
            tHigh = fahrenheit
        if fahrenheit < tLow:
            tLow = fahrenheit
        webiopi.debug("Low:     %0.1f°F" % tLow)
        webiopi.debug("High:    %0.1f°F" % tHigh)

        # Temperature thresholds
        webiopi.debug("Cold Threshold:    %0.1f°F" % COLD)
        webiopi.debug("Hot Threshold:     %0.1f°F" % HOT)
      
        # Toggle State (Current or Range)
        global displayCurrent
        displayCurrent = not displayCurrent

 
        # Check for reset switch press
        if GPIO.digitalRead(SWITCH) == GPIO.LOW:
            tHigh = fahrenheit
            tLow = fahrenheit
            setColor(Colors['White'])
            lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
            lcd.lcd_string("Current: %0.1f" % (fahrenheit)  + chr(223) + "F")
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string("Temp Range Reset")
        elif displayCurrent:
            # Current temp state (text color based on thresholds)
            if fahrenheit >= HOT:
                setColor(Colors['Red'])
            elif fahrenheit <= COLD:
                setColor(Colors['Blue'])
            else:
                setColor(Colors['Green'])
            # Display current temp
            lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
            lcd.lcd_string("Current: %0.1f" % (fahrenheit)  + chr(223) + "F")
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string(" ")
        else:
            # Temp range state (text color based on thresholds)
            if fahrenheit >= HOT:
                setColor(Colors['Orange'])
            elif fahrenheit <= COLD:
                setColor(Colors['Violet'])
            else:
                setColor(Colors['Aquamarine'])
            # Display temp range
            lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
            lcd.lcd_string("Low:  %0.1f" % (tLow)  + chr(223) + "F")
            lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
            lcd.lcd_string("High: %0.1f" % (tHigh)  + chr(223) + "F")
    except:
        webiopi.debug("error: " + str(sys.exc_info()[0]))
    finally:
        webiopi.sleep(5)  

		
# Called by WebIOPi at server shutdown
def destroy():
    webiopi.debug("Script with macros - Destroy")
    # Reset GPIO functions
    GPIO.setFunction(RED, GPIO.IN)
    GPIO.setFunction(GREEN, GPIO.IN)
    GPIO.setFunction(BLUE, GPIO.IN)
    GPIO.setFunction(SWITCH, GPIO.IN)

	
# A macro to reset temperature range from web
@webiopi.macro
def ResetTempRange():
    webiopi.debug("Reset Temp Range Macro...")
    global tHigh
    global tLow
    fahrenheit = t.getFahrenheit()
    tHigh = fahrenheit
    tLow = fahrenheit
    setColor(Colors['Cyan'])
    # Display current temperature on LCD display
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("Temp Range Reset")
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string("( HTTP Request )")


# A macro to get the sensor temperature from web
@webiopi.macro
def GetSensorTemp():
    webiopi.debug("GetSensorTemp Macro...")
    # Get current temperature
    fahrenheit = t.getFahrenheit()
    setColor(Colors['Purple'])
    # Display current temperature on LCD display
    lcd.lcd_byte(lcd.LCD_LINE_1, lcd.LCD_CMD)
    lcd.lcd_string("Current: %0.1f" % (fahrenheit)  + chr(223) + "F")
    lcd.lcd_byte(lcd.LCD_LINE_2, lcd.LCD_CMD)
    lcd.lcd_string("( HTTP Request )")
    return "Current:  %0.1f°F\r\nLow:      %0.1f°F\r\nHigh:     %0.1f°F" % (fahrenheit, tLow, tHigh)

