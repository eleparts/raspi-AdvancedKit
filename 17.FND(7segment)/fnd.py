import RPi.GPIO as GPIO
import time 

GPIO.setwarnings(False)

Ds = 4      # 14pin
STCP = 5    # 12pin
SHCP = 6    # 11pin

GPIO.setmode(GPIO.BCM)
GPIO.setup(Ds,GPIO.OUT)         # GPIO 출력설정
GPIO.setup(STCP,GPIO.OUT)
GPIO.setup(SHCP,GPIO.OUT)

list = [
    [0,0,1,1,1,1,1,1],   #0
    [0,0,0,0,0,1,1,0],   #1
    [0,1,0,1,1,0,1,1],   #2 
    [0,1,0,0,1,1,1,1],   #3
    [0,1,1,0,0,1,1,0],   #4
    [0,1,1,0,1,1,0,1],   #5
    [0,1,1,1,1,1,0,1],   #6
    [0,0,0,0,0,1,1,1],   #7
    [0,1,1,1,1,1,1,1],   #8
    [0,1,1,0,0,1,1,1],   #9
]

while 1:                             # 무한 반복
    for y in range(10):
        for x in list[y]:
            GPIO.output(Ds,x)              # 데이터 비트 넣기
            time.sleep(0.001)              # 대기
            GPIO.output(STCP,1)            # 클럭 핀 HIGH
            time.sleep(0.001)
            GPIO.output(STCP,0)            # 클럭 핀 LOW rising 엣지에 넣기
            GPIO.output(Ds,0)              # 데이터 비트 초기화
            GPIO.output(SHCP,1)            # 8비트 병렬로 쉬프트하기
            time.sleep(0.001)
            GPIO.output(SHCP,0)            # 쉬프트 핀 LOW
            
        time.sleep(1.5)