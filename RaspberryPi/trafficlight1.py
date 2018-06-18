# Traffic Light 1: Emulate a single direction traffic light
# Programmed by Precilla
# Program date 06.17.2018

import RPi.GPIO as GPIO
import time

redLight1 = 17 # our red light (LED) pin
yellowLight1 = 27 # our yellow light (LED) pin
greenLight1 = 22 # our green light (LED) pin
redDelay = 30/10 # delay for red light (seconds)
yellowDelay = 5/10 # delay for yellow light (seconds)
greenDelay = 25/10 # delay for green light (seconds)

GPIO.setmode(GPIO.BCM) # Sets the GPIO mapped on the R-Pi
GPIO.setup(redLight1, GPIO.OUT) # Set pin as output
GPIO.setup(yellowLight1, GPIO.OUT) # Set pin as output
GPIO.setup(greenLight1, GPIO.OUT) # Set pin as output

GPIO.output(redLight1, GPIO.LOW) # turn off the red
GPIO.output(yellowLight1, GPIO.LOW) # turn off the yellow
GPIO.output(greenLight1, GPIO.LOW) # turn off the green 

while True: # repeat indefinitely
    print ('Red Light') # send text to the screen
    GPIO.output(redLight1, GPIO.HIGH) # turn on red light
    GPIO.output(yellowLight1, GPIO.LOW) # turn off yellow light
    time.sleep(redDelay) # wait for red cycle
    print ('Green Light') # send text to the screen
    GPIO.output(greenLight1, GPIO.HIGH) # turn on green light
    GPIO.output(redLight1, GPIO.LOW) # turn off red light
    time.sleep(greenDelay) # wait for green cycle
    print ('Yellow Light') # send text to the screen
    GPIO.output(yellowLight1, GPIO.HIGH)# turn on yellow light
    GPIO.output(greenLight1, GPIO.LOW) # turn off green light
    time.sleep(yellowDelay) # wait for yellow cycle