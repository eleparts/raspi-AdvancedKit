import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)

clk     = 17
dt      = 18
red     = 23
blue    = 22
orange  = 11

list    = [clk,dt]
list_2  = [red,blue,orange]
GPIO.setmode(GPIO.BCM)

for i in list:
    GPIO.setup(i, GPIO.IN, GPIO.PUD_DOWN)   # [clk,dt] 입력, 내부 풀 다운 설정

for j in list_2:
    GPIO.setup(j,GPIO.OUT)                  # [red,blue,orange] 출력 설정

clkLastState = GPIO.input(clk)
counter = 0
is_running = True

try:
    while is_running:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)

        if clkState != clkLastState:    # clkState와 clkLastState가 같지 않으면
            if dtState != clkState:     # clkState와 dtState가 같지 않으면
                counter += 1                # counter 증가
            else:
                counter -= 1                # counter 감소
            print(counter)              # counter 출력
            clkLastState = clkState     # 마지막 clk의 상태와 현재 clk의 상태를 같게 만들어줌
            time.sleep(0.01)

        if counter<=-10:    # counter값이 -10보다 작으면 빨간색 LED ON

            GPIO.output(red,GPIO.HIGH)
            GPIO.output(blue,GPIO.LOW)
            GPIO.output(orange,GPIO.LOW)

        elif counter<10:    # counter값이 -10보다 작으면 주황색 LED ON
        
            GPIO.output(red,GPIO.LOW)
            GPIO.output(blue,GPIO.HIGH)
            GPIO.output(orange,GPIO.LOW)

        else:               # counter값이 -10보다 작으면 파란색 LED ON

            GPIO.output(red,GPIO.LOW)
            GPIO.output(blue,GPIO.LOW)
            GPIO.output(orange,GPIO.HIGH)

except KeyboardInterrupt:

    GPIO.cleanup()
    is_running = False