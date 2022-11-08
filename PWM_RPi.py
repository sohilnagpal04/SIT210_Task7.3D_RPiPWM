
from gpiozero import LED
import RPi.GPIO 
import time
import RPi.GPIO as GPIO
RPi.GPIO.setmode(RPi.GPIO.BCM)
GPIO.setwarnings(False)

GPIO_TRIGGER = 18
GPIO_ECHO = 24

GPIO.setup(12, GPIO.OUT)

led = GPIO.PWM(12, 1000)
led.start(0)

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

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
 
    return int(distance)

try:
    while True:
        dis = Distance()
        print ("Distance = " + str(dis) + " cm")
        if dis < 50:
                led.ChangeDutyCycle((50 - dis)*2)
        else:
            led.start(0)

        time.sleep(1)
 
except KeyboardInterrupt:
    GPIO.cleanup()

