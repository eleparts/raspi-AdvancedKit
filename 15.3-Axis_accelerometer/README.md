# 라즈베리파이 고급 키트 - 기울기 센서(ADXL345)  

블로그 바로가기 : [라즈베리파이 고급 키트 - 기울기 센서(ADXL345)](https://blog.naver.com/elepartsblog/221532166120)  

## 회로 연결  

자세한 사항은 블로그 설명을 참고해 주세요.  

![3-Axis_accelerometer](https://blogfiles.pstatic.net/MjAxOTA1MDhfMTU3/MDAxNTU3MjczOTQ1NDMz.NgPa31Cb9ysLPwsua_F6PWLZD1axfMztRzqfpIJR6cIg.0mIzRBRUnfUDXsVSzNHsINgVXdcvbvhAsf9l6UC2IaUg.PNG.elepartsblog/2.PNG?type=w2)  

## 예제 실행  

### GUI 환경에서 실행  

라이브러리 다운로드, 설치등의 과정이 있어 터미널 환경에서 실행해 주도록 합니다.  

### CLI (터미널)환경에서 실행  

터미널 창에서 아래의 명령어로 설치&실행해 줍니다.  

```bash
sudo apt-get install git build-essential python-dev

git clone https://github.com/adafruit/Adafruit_Python_ADXL345
cd Adafruit_Python_ADXL345
sudo python setup.py install

# or

sudo pip3 install adafruit-adxl345
```

예제 실행  

```bash
cd examples
#cd Adafruit_Python_ADXL345/examples

sudo python3 simpletest.py
```
