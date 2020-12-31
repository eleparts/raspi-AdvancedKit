import RPi.GPIO as GPIO
import time

sw  = 16
led = 24

GPIO.setmode(GPIO.BCM)

GPIO.setup(sw,GPIO.IN,GPIO.PUD_DOWN)    # 내장 풀다운 사용
GPIO.setup(led,GPIO.OUT)

try:
    while 1:
        if GPIO.input(sw)==1:           # 스위치 감지
            GPIO.output(led,GPIO.HIGH)
        else :
            GPIO.output(led,GPIO.LOW)

except KeyboardInterrupt:
    GPIO.cleanup()