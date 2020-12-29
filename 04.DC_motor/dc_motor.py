import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)   # 사용중인 pin 에러메시지 출력 해제
GPIO.setmode(GPIO.BCM)

A = 23  # 모터 A핀
B = 24  # 모터 B핀

GPIO.setup(A,GPIO.OUT) # A,B GPIO setup설정
GPIO.setup(B,GPIO.OUT)

try:
    while 1:
        GPIO.output(A,GPIO.HIGH)    # 오른쪽 회전
        GPIO.output(B,GPIO.LOW)
        time.sleep(5)               # 5초 유지

        GPIO.output(A,GPIO.LOW)     # 정지
        GPIO.output(B,GPIO.LOW)  
        time.sleep(2)               # 2초 유지

        GPIO.output(A,GPIO.LOW)     # 왼쪽 회전
        GPIO.output(B,GPIO.HIGH)
        time.sleep(5)               # 5초 유지

        GPIO.output(A,GPIO.LOW)     # 정지
        GPIO.output(B,GPIO.LOW)  
        time.sleep(2)               # 2초 유지

except KeyboardInterrupt:       # Ctrl+c => 종료
    
    GPIO.output(A,GPIO.LOW) 
    GPIO.output(B,GPIO.LOW)
    
    GPIO.cleanup()                # GPIO 점유 리소스 해제
