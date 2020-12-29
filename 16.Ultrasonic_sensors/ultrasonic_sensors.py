import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO_TRIGGER  = 23
GPIO_ECHO     = 24

print("start")

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

try:
    while True:

        # 트리거 핀 high 설정
        GPIO.output(GPIO_TRIGGER, True)

        # 0.00001초 sleep 후 트리거 핀 low 설정
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)

        StartTime = time.time()
        StopTime = time.time()

        # 시작 시간 저장
        while GPIO.input(GPIO_ECHO) == 0:
            StartTime = time.time()

        # 마지막 시간 저장
        while GPIO.input(GPIO_ECHO) == 1:
            StopTime = time.time()

        # 시작 시간과 마지막 시간의 차이 계산, 저장
        TimeElapsed = StopTime - StartTime

        # 음속을 곱해 거리 계산, 2로(왕복) 나누기
        distance = round((TimeElapsed * 34300) / 2, 2)

        # 계산된 거리 출력
        print ("Distance = " , distance)
        time.sleep(1)

except KeyboardInterrupt:

    GPIO.cleanup()

