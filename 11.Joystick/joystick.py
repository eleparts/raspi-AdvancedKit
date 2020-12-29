import smbus
import time

# i2c 통신에 사용하는 함수
bus = smbus.SMBus(1)

def setup(Addr):        # 주소 설정

    global address      # 전역 변수
    address = Addr


def read(chn):                          # channel

    if chn == 0:                        # Ain0채널
        bus.write_byte(address,0x40)    # (주소, 명령어) 주소에 명령어 전달

    if chn == 1:                        # Ain1채널
        bus.write_byte(address,0x41)

    bus.read_byte(address)              # 주소의 값 읽어오기

    return bus.read_byte(address)       # 읽어온 값 반환


try:
    setup(0x48)                   # i2c 주소 입력

    while True:
        print ('AIN0 = ', read(0))  # X축 출력
        print ('AIN1 = ', read(1))  # Y축 출력
        time.sleep(0.5)

except KeyboardInterrupt:
    pass