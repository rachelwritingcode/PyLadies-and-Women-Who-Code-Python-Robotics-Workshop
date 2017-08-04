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
GPIO.setup(13, GPIO.OUT)
# blink GPIO17 2 times
for i in range(0,2):
        blink(13)
GPIO.cleanup()

"""
Credits to Rahul Kar for base code
http://www.rpiblog.com/2012/09/using-gpio-of-raspberry-pi-to-blink-led.html
"""
