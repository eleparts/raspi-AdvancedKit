import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
SCL = 21
SDO = 20

GPIO.setmode(GPIO.BCM)

GPIO.setup(SCL,GPIO.OUT)
GPIO.setup(SDO,GPIO.IN,GPIO.PUD_DOWN)

is_running = True 

def Read_Keypad(): # 키패드 입력 감지 함수

    result = 0

    for i in range(1,17):           # 1부터 17까지
        GPIO.output(SCL,GPIO.LOW)

        if GPIO.input(SDO) == 0:    # SDO가 0이면
            result = i              # result는 i

        GPIO.output(SCL,GPIO.HIGH)

    return result                   # result 반환


try:
    while is_running:

        value=Read_Keypad() # result값 저장

        if value != 0:      # result가 0이 아니면
            print(value)    # result 출력
            time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    is_running=False