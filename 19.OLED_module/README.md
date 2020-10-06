# 라즈베리파이 고급 키트 - 0.96inch OLDE 모듈

블로그 바로가기 : [라즈베리파이 고급 키트 - 0.96inch OLDE 모듈](https://blog.naver.com/elepartsblog/221551346359)  

## 회로 연결  

자세한 사항은 블로그 설명을 참고해 주세요.  

| OLED | 라즈베리파이 PIN 번호 |
|------|-------------|
| VCC  | 3.3V        |
| GND  | GND         |
| SDA  | 3 (SDA)     |
| SCL  | 5 (SCL)     |

- 위 PIN 번호는 GPIO 핀 40개의 순서 번호(3.3V 1번, 5V 2번...)로, BCM 핀 번호는 2,3 번 입니다.

## 예제 실행  

### GUI 환경에서 실행  

라이브러리 다운로드, 설치등의 과정이 있어 터미널 환경에서 실행해 주도록 합니다.  

### CLI (터미널)환경에서 실행  

블로그를 참고하여 아래의 명령어로 실행해 줍니다.  

블로그에서는 이미지를 직접 제작, 라즈베리파이로 옮겨 사용하지만 아래 예제에서는 샘플 이미지 파일을 같이 제공하고 있어 이미지 파일 제작을 하지 않아도 진행 가능합니다.  

모듈 사용을 위해 **라즈베리파이 설정에서 `I2C를 Enable`** 해 줍니다.  

```bash
# 모듈 정상 연결 여부 확인 (I2C 주소 출력)
i2cdetect -y 1
```

아래 명령어로 예제 다운로드 및 라이브러리 설치, 예제를 실행해 볼 수 있습니다.  

```bash
# 예제 다운로드  
git clone https://github.com/adafruit/Adafruit_CircuitPython_SSD1306/

# 라이브러리 설치 (pip3)
sudo pip3 install adafruit-blinka
sudo pip3 install adafruit-circuitpython-ssd1306

# 예제 디렉토리로 이동
cd Adafruit_CircuitPython_SSD1306/examples

# 이미지 출력 예제
sudo python3 ssd1306_pillow_images.py
```
