# Import GPIO Library
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

# Define GPIO pins being used
GPIO_TRIGGER = 18 
GPIO_ECHO = 25  

#Trig will send out a short burst of sound waves
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  
#Echo will listen for waves that bounce back
GPIO.setup(GPIO_ECHO,GPIO.IN)      

GPIO.output(GPIO_TRIGGER, False)
# Wait for sensor to settle
time.sleep(1)

# Send out pulse
GPIO.output(GPIO_TRIGGER, True)
#Wait 10 microseconds so the pulse
#can be read by the sensor (the sensor expects 10Us)
time.sleep(0.00001)
#Stop the pulse 
GPIO.output(GPIO_TRIGGER, False)

pulse_start = time.time()

#Determine what values echo will measure

#Listen to echo, 0 means no pulse has been sent back 
while GPIO.input(GPIO_ECHO) == 0:
#Records the time
  pulse_start = time.time()

#Listen to echo, 1 means a pulse has been sent back to echo
while GPIO.input(GPIO_ECHO) == 1:
#Records the time
  pulse_stop = time.time()

# Calculate pulse duration by subtracting the two 
#different measurements from echo
pulse_duration = pulse_stop-pulse_start

#Convert distance into centimetres 
distance = pulse_duration * 17000

#Round the distance up to nearest 2 decimals
distance = round(distance, 2)

#Print out a message for each of the different distance values

#if distance is less than 10
if distance < 10:
	print "The distance is less than 10 cms"
#if distance is less than 20
elif distance < 20:
	
#if distance is less than 30
elif distance < 30:

#else print the distance is over 30 cms
else:
	
#exit the program
GPIO.cleanup()

"""
Credits to ModMyPi.com for base code
https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
"""

