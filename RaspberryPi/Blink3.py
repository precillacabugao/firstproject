# Blink3: blink an LED when a button is pressed  
# Programmed by Precilla Cabugao
# Program date 06/17/2018

import RPi.GPIO as GPIO
import time

LEDpin = 17 # the GPIO pin we will use as an output
delay = 0.5 # number of seconds to wait between changes
Btnpin = 15 # the GPIO pin we will use as an input
PRESSED = 0 # Readability ‘button press happened’

GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(LEDpin, GPIO.OUT) # Set GPIO17 (pin 11) as output
GPIO.setup(Btnpin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 # Set GPIO22 (pin 15) as input with pull-up 

while True: # repeat indefinitely
    if GPIO.input(Btnpin)==PRESSED:
        # if the Btnpin is pressed, blink
        print ('on') # send 'on' to the screen
        GPIO.output(LEDpin, GPIO.HIGH) # turn on LEDpin
        time.sleep(delay) # wait
        print ('off') # send 'off' to the screen
        GPIO.output(LEDpin, GPIO.LOW) # turn off LEDpin
        time.sleep(delay) # wait 