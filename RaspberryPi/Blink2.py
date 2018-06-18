# Blink2: blink an LED connected to the GPIO port using variables  
# Programmed by Precilla Cabugao
# Program date 06/17/2018

import RPi.GPIO as GPIO
import time

LEDpin = 17 # the GPIO pin we will use as an output
delay = 0.5 # number of seconds to wait between changes

GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(LEDpin, GPIO.OUT) # Set GPIO17 (pin 11) as output 

while True:
    print ('on') # send 'on' to the screen
    GPIO.output(LEDpin, GPIO.HIGH) # turn on GPIO17
    time.sleep(delay) # wait 1/2 second
    print ('off') # send 'off' to the screen
    GPIO.output(LEDpin, GPIO.LOW) # turn off GPIO17
    time.sleep(delay) # wait 1/2 second