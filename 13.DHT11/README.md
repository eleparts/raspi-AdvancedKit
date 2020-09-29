# 라즈베리파이 고급 키트 - DHT11(온습도센서)  

블로그 바로가기 : [라즈베리파이 고급 키트 - DHT11(온습도센서)](https://blog.naver.com/elepartsblog/221525069011)  

## 회로 연결  

자세한 사항은 블로그 설명을 참고해 주세요.  

![dht11](https://blogfiles.pstatic.net/MjAxOTA0MjlfMTY3/MDAxNTU2NTAwMDA4NDgx.Av6EbvwOMICIlTZP5XB62Qwak0XCGEHZSh9NcNS3jJMg.sYhG_NjwiVal9QNUa9fDohET7YY3ZT9inTorZMHh-xgg.PNG.elepartsblog/2.PNG?type=w2)  

## 예제 실행  

### GUI 환경에서 실행  

라이브러리 다운로드, 설치등의 과정이 있어 터미널 환경에서 실행해 주도록 합니다.  

### CLI (터미널)환경에서 실행  

터미널 창에서 아래의 명령어로 설치&실행해 줍니다.  

```bash
# Adafruit 라이브러리 공통 패키지 설치
sudo apt-get update  
sudo apt-get install -y python3 python3-pip python-dev  
sudo pip3 install rpi.gpio

# DHT 라이브러리 패키지 설치
sudo apt-get install build-essential python-dev

# DHT 소스 코드 다운로드 및 설치 (Adafruit_Python_DHT 저장소 다운로드 )
git clone https://github.com/adafruit/Adafruit_Python_DHT.git  

cd Adafruit_Python_DHT

sudo python setup.py install
```

예제코드 실행  

```bash
# 예제코드 디렉토리로 이동
cd examples

# 예제 코드 실행 / 11 2 : DHT11 , GPIO BCM P2
sudo ./AdafruitDHT.py 11 2
```
