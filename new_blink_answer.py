#full code for new_blink.py

#import the GPIO Library
import RPi.GPIO as GPIO
import time
# blinking function

def blink(pin):
        #Setting the LED to turn on 
        GPIO.output(pin,GPIO.HIGH)
        time.sleep(1)
        #Setting the LED to turn off
        GPIO.output(pin,GPIO.LOW)
        time.sleep(1)
        return
		
# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)
# set up GPIO output channel
GPIO.setup(15, GPIO.OUT)
# blink GPIO17 2 times
for i in range(0,2):
        blink(15)
GPIO.cleanup()

