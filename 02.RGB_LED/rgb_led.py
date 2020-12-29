import RPi.GPIO as GPIO
import time

# 빨, 주, 노, 초, 파, 남, 보
colors = [0xFF0000, 0xFF0023, 0xFF00FF, 0x0000FF, 0x00FF00, 0x64EB00, 0x4BFB00]
pins = {'pin_R':11, 'pin_G':9, 'pin_B':10}  # 핀 지정   △ // 11 9 10

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)            # GPIO BCM 모드 설정

for i in pins:
    GPIO.setup(pins[i], GPIO.OUT)   # 핀 모드를 출력으로 설정
    GPIO.output(pins[i], GPIO.HIGH) # LED를 HIGH로 설정해서 LED 끄기

p_R = GPIO.PWM(pins['pin_R'], 2000)  # 주파수 설정 2KHz
p_G = GPIO.PWM(pins['pin_G'], 2000)
p_B = GPIO.PWM(pins['pin_B'], 2000)

p_R.start(0)      # 초기 듀티 사이클 = 0 (LED 끄기)
p_G.start(0)
p_B.start(0)

def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# LED 색을 설정하는 함수
def setColor(col):   # 예)  col = 0x112233

    R_val = (col & 0x110000) >> 16
    G_val = (col & 0x001100) >> 8
    B_val = (col & 0x000011) >> 0

    R_val = map(R_val, 0, 255, 0, 100)
    G_val = map(G_val, 0, 255, 0, 100)
    B_val = map(B_val, 0, 255, 0, 100)

    p_R.ChangeDutyCycle(100-R_val)      # 듀티 사이클 변경
    p_G.ChangeDutyCycle(100-G_val)
    p_B.ChangeDutyCycle(100-B_val)


try:
    while True:                         # 무한 반복  
        for col in colors:
            setColor(col)
            time.sleep(1.0)

except KeyboardInterrupt:               # Ctrl+c로 종료
    p_R.stop()
    p_G.stop()
    p_B.stop()

    for i in pins:
        GPIO.output(pins[i], GPIO.HIGH)   # LED 끄기
        GPIO.cleanup()

