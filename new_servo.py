import RPi.GPIO as GPIO
import time
import os

GPIO.setwarnings(False)
# Set the layout for the pin declaration
GPIO.setmode(GPIO.BOARD)
# The pin 11 is the out pin for the PWM signal for the servo.
GPIO.setup(11, GPIO.OUT)

# Options to run your program
print "l = move to the left"
print "r = move to the right"
print "q = stop and exit"


while True:
	#Set servo to 50Mhz
	Servo = GPIO.PWM(11, 50)						
	#start servo
	Servo.start(0)

	#Ask what direction to go
	input = raw_input("What direction should I go?: ") 

	# 12.5 is the value for a 180 degree move to the right
	# 2.5 is the value for a -90 degree move to the left
	
	#If q is pressed, quit the program
	if(input == "q"):
		print "Stopping the program "
		os._exit(1)
		Servo.stop()
		GPIO.cleanup()

	#If r is pressed turn servo right 
	elif(input == "r"):
		#print a notification that the servo is turning right		

		Servo.ChangeDutyCycle(2.5)
		#turn servo right for 5 seconds
		time.sleep(5)
		Servo.stop()

	#If l is pressed turn servo left
	elif(input == "l"):
		#print a notification that the servo is turning left

		Servo.ChangeDutyCycle(12.5)
		#turn servo left for 5 seconds
		time.sleep(5)
		Servo.stop()	
		
	#Print am error message if none of the options are selected
	else:
		print "Whoops you must choose l,r or q to run this program"

"""
Credits to Ingmar Stapel for base code 
http://www.raspberry-pi-car.com/top-story-en/raspberry-pi-controlling-servo-motors/7028
"""
