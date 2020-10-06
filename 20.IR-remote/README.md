# 라즈베리파이 고급 키트 - IR 수신기

블로그 바로가기 : [라즈베리파이 고급 키트 - IR 수신기](https://blog.naver.com/elepartsblog/221558430782)  

## 회로 연결  

자세한 사항은 블로그 설명을 참고해 주세요.  

![ir-receiver](https://blogfiles.pstatic.net/MjAxOTA2MDdfMjAw/MDAxNTU5ODk1NTcwMjY4.qkdgOVPLJ7hkjRQTfYRBj_zAX4lUkW9QnpSYkQil5VQg.ZUC1Qmy6JO6tQwXmWkWCTH3Z4CzMJyt0sQu3RptG72Ag.PNG.elepartsblog/10.PNG?type=w2)  

## 예제 실행  

### GUI 환경에서 실행  

라이브러리 다운로드, 설치등의 과정이 있어 터미널 환경에서 실행해 주도록 합니다.  

### CLI (터미널)환경에서 실행  

LIRC 라이브러리를 설치, 사용해 줍니다.  

```bash
# lirc 설치
sudo apt-get install lirc liblircclient-dev

sudo nano /boot/config.txt
# 아래 내용을 추가해 줍니다. - BCM GPIO 18 (#18) 핀을 입력으로 사용
dtoverlay=gpio-ir,gpio_pin=18


sudo nano /etc/lirc/lirc_options.conf
# 아래 내용으로 수정해 줍니다.
driver = default
device = /dev/lirc0
```

리모컨 입력 테스트  

```bash
sudo mode2 -d /dev/lirc0
```

mode2 를 실행 후 리모컨의 버튼을 IR 수신기를 향해 누르면 메세지가 출력(입력 신호의 값)되는 것을 확인할 수 있습니다.  

이후 irrecord로 리모컨을 등록할 수 있으나, 해당 부분에 대해서는 버전 변경 등으로 정상 진행되지 않는 문제가 있어 여기서는 진행하지 않겠습니다.  

- 리모컨 등록은 아래 명령으로 진행하나 버전 문제 등으로 정상 동작하지 않는 문제가 있습니다.  

```bash
# 지정가능한 키 이름 목록
irrecord --list-namespace

# 리모컨 수동 등록 / 오작동  
irrecord -d /dev/lirc0
#irrecord -f -d /dev/lirc0
```
