#including the required libraries
from gpiozero import LED
import RPi.GPIO 
import time
import RPi.GPIO as GPIO

RPi.GPIO.setmode(RPi.GPIO.BCM)      #setting the gpio mode to BCM
GPIO.setwarnings(False)

GPIO_TRIGGER = 18       #setting the trigger pin of ultrasonic sensor
GPIO_ECHO = 24          #setting the echo pin of ultrasonic sensor

GPIO.setup(12, GPIO.OUT)    #initialising the led pin 12

led = GPIO.PWM(12, 1000)        #setting the led pin as PWM 
led.start(0)    #led initial state low

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)      #initialising the trigger pin
GPIO.setup(GPIO_ECHO, GPIO.IN)          #initialising the echo pin

#creating a function distance to read and return the distance from ultrasonic sensor.
def Distance():
    GPIO.output(GPIO_TRIGGER, True)
 
    time.sleep(0.001)
    GPIO.output(GPIO_TRIGGER, False)
 
    time_start = time.time()
    time_stop = time.time()
  
    while GPIO.input(GPIO_ECHO) == 0:
        time_start = time.time()
 
    while GPIO.input(GPIO_ECHO) == 1:
        time_stop = time.time()
 
    TimeElapsed = time_stop - time_start
    distance = (TimeElapsed * 34300) / 2
 
    return int(distance)        #returning the distance in integer.

try:
    while True:
        dis = Distance()        #reading the distance using above function
        print ("Distance = " + str(dis) + " cm")        #printing the distance in cm
        if dis < 50:
                led.ChangeDutyCycle((50 - dis)*2)   #changing the duty cycle of the led if distance is < 50
        else:
            led.start(0)    #led turning off if the distance in more than 50.

        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()

