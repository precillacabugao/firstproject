# Coffin (AND example) program
# programmed by Precilla
# Program date 06/17/2018

import RPi.GPIO as GPIO
import time 

coffinBtn= 17 # Pin for our tour guide button
coffinSensor = 22 # Pin for our proximity detector
doorSwing = 10 # Pin for our door solenoid
tourReady = 1 # Input from our coffinBtn pin
doorClear = 1 # Input from our coffinSensor pin
PRESSED = 0 # Readability ‘button press happened’

# setup IO pins
GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(coffinBtn, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 # Set GPIO pin for input from Tour Button
GPIO.setup(coffinSensor, GPIO.IN, pull_up_down=GPIO.PUD_UP)
 # Set GPIO pin for input from coffin door sensor
GPIO.setup(doorSwing, GPIO.OUT) # GPIO pin for the door mech.

while True:
    tourReady = GPIO.input(coffinBtn) # Tour guide’s button
    doorClear = GPIO.input(coffinSensor) # proximity sensor
    if tourReady == PRESSED and doorClear == PRESSED:
        # if both are true
        GPIO.output(doorSwing, GPIO.HIGH) # open the coffin door
        time.sleep(3) # wait ten seconds
        GPIO.output(doorSwing, GPIO.LOW) # close the coffin door