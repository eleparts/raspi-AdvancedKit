# 라즈베리파이 고급 키트 - 0.96inch OLDE 모듈

블로그 바로가기 : [라즈베리파이 고급 키트 - 0.96inch OLDE 모듈](https://blog.naver.com/elepartsblog/221551346359)  

## 회로 연결  

자세한 사항은 블로그 설명을 참고해 주세요.  

| OLED | 라즈베리파이 |
|------|-------------|
| VCC  | 3.3V |
| GND  | GND  |
| SCL  | 5    |
| SDA  | 3    |

## 예제 실행  

### GUI 환경에서 실행  

라이브러리 다운로드, 설치등의 과정이 있어 터미널 환경에서 실행해 주도록 합니다.  

### CLI (터미널)환경에서 실행  

블로그를 참고하여 아래의 명령어로 실행해 줍니다.  

블로그에서는 이미지를 직접 제작, 라즈베리파이로 옮겨 사용하지만 예제에서 샘플 파일을 같이 제공하고 있어 이미지 파일 제작을 하지 않아도 진행 가능합니다.  

```bash
sudo python -m pip install --upgrade pip setuptools wheel

sudo pip install Adafruit-SSD1306

# 예제 다운로드  
git clone https://github.com/adafruit/Adafruit_Python_SSD1306

cd Adafruit-SSD1306/example

# 도형 출력  
sudo python shapes.py

# 이미지 출력  
sudo python image.py
```
