
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(16,GPIO.OUT)
p=GPIO.PWM(16,50)
p.start(7.5)
try:
    while True:
        p.ChangeDutyCycle(7.5)#Neutral
        time.sleep(1)
        p.ChangeDutyCycle(12.5)#180
        time.sleep(1)
        p.ChangeDutyCycle(2.5)#0
        time.sleep(1)

except KeyboardInterrupt:
        p.stop()
        GPIO.Cleanup()
