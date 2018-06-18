# Blink: blink an LED connected to the GPIO port
# Programmed by Precilla Cabugao
# June 16, 2018

import RPi.GPIO as GPIO
import time
print ("Hello")

GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(17, GPIO.OUT) # Set GPIO17 (pin 11) as output 

while True:
    #print ('on') # send 'on' to the screen
    GPIO.output(17, GPIO.HIGH) # turn on GPIO17
    time.sleep(2.0/10) # wait 1/2 second
    #print ('off') # send 'off' to the screen
    GPIO.output(17, GPIO.LOW) # turn off GPIO17
    time.sleep(3.4/10) # wait 1/2 second