# Traffic Light 2: Emulate a bi-direction traffic light
# Programmed by Precilla
# Program date 06.17.2018

import RPi.GPIO as GPIO
import time

redLight1 = 17 # our red light (LED) pin
yellowLight1 = 27 # our yellow light (LED) pin
greenLight1 = 22 # our green light (LED) pin
#redDelay = 30/10 # delay for red light (seconds)
yellowDelay = 5/10 # delay for yellow light (seconds)
greenDelay = 25/10 # delay for green light (seconds)
redLight2 = 10 # second red light (LED)
yellowLight2 = 9 # second yellow light (LED)
greenLight2 = 11 # second green light (LED)


GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(redLight1, GPIO.OUT) # Set pin as output
GPIO.setup(yellowLight1, GPIO.OUT) # Set pin as output
GPIO.setup(greenLight1, GPIO.OUT) # Set pin as output
GPIO.setup(redLight2, GPIO.OUT) # Set pin as output
GPIO.setup(yellowLight2, GPIO.OUT) # Set pin as output
GPIO.setup(greenLight2, GPIO.OUT) # Set pin as output

GPIO.output(redLight1, GPIO.LOW) # turn off the red
GPIO.output(yellowLight1, GPIO.LOW) # turn off the yellow
GPIO.output(greenLight1, GPIO.LOW) # turn off the green
GPIO.output(redLight2, GPIO.LOW) # turn off red 2
GPIO.output(yellowLight2, GPIO.LOW) # turn off yellow 2
GPIO.output(greenLight2, GPIO.LOW) # turn off green 2

while True: # repeat indefinitely
    print ('Red Light 1') # send text to the screen
    print ('Green Light 2') # send text to the scree
    GPIO.output(redLight1, GPIO.HIGH) # turn on red light 1
    GPIO.output(greenLight2, GPIO.HIGH) # turn on green light 2
    GPIO.output(yellowLight1, GPIO.LOW) # turn off yellow light
    GPIO.output(redLight2, GPIO.LOW) # turn off red light 2
    time.sleep(greenDelay) # wait for green cycle
    print ('Yellow Light 2') # send text to the screen
    GPIO.output(yellowLight2, GPIO.HIGH)# turn on yellow light 2
    GPIO.output(greenLight2, GPIO.LOW) # turn off green light 2
    time.sleep(yellowDelay) # wait for yellow cycle
    print ('Red Light 2') # send text to the screen
    print ('Green Light 1') # send text to the scree
    GPIO.output(redLight2, GPIO.HIGH) # turn on red light 2
    GPIO.output(greenLight1, GPIO.HIGH) # turn on green light 1
    GPIO.output(yellowLight2, GPIO.LOW) # turn off yellow light
    GPIO.output(redLight1, GPIO.LOW) # turn off red light 1
    time.sleep(greenDelay) # wait for green cycle
    print ('Yellow Light 1') # send text to the screen
    GPIO.output(yellowLight1, GPIO.HIGH)# turn on yellow light 1
    GPIO.output(greenLight1, GPIO.LOW) # turn off green light 1
    time.sleep(yellowDelay) # wait for yellow cycle