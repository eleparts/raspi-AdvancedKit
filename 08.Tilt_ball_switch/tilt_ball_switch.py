import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

b_sw    = 16
led_r   = 24
led_b   = 23

GPIO.setmode(GPIO.BCM)

GPIO.setup(b_sw,GPIO.IN,GPIO.PUD_DOWN)  # 내부 풀 다운 사용
GPIO.setup(led_r,GPIO.OUT)
GPIO.setup(led_b,GPIO.OUT)

def turn_ledB(self):                    # 함수 만들기 / (self) = 받아오는 인자가 없을 때 void의 의미
    GPIO.output(led_b,GPIO.HIGH)
    time.sleep(1)
    GPIO.output(led_b,GPIO.LOW)

GPIO.add_event_detect(b_sw,GPIO.FALLING,turn_ledB) # 인터럽트 사용

'''
GPIO.add_event_detect(channel,edge,callback=none,bouncetime=none)
channel : 입력으로 설정된 GPIO 번호
edge : 이벤트 실행 신호 (RISING,FALLING,BOTH)
callback : 이벤트 발생 시 호출할 함수
bouncetime : 이 시간 동안 한 번의 이벤트만 실행
'''

try:
    while 1:
        GPIO.output(led_r,GPIO.HIGH)
        time.sleep(0.5)

        GPIO.output(led_r,GPIO.LOW)
        time.sleep(0.5)

except KeyboardInterrupt:         # ctrl+c 종료
    GPIO.cleanup()

 