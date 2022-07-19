# capstone2022_1
# 요약
 2022년 1학기 정일엽 교수님 캡스톤 디자인 수업 'light24'조의 코드 파일입니다. CCTV로부터 받아온 영상 정보로부터 객체탐지를 시행하여 사람이 있는지 없는지를 탐지하고, 매장 내의 조명을 조절하여 에너지를 관리하는 프로젝트입니다. 2022년 여수 엑스포에서 열리는 스마트 에너지 경진대회에서 금상을 수상하였습니다.  
 ![대회 사진](https://github.com/uichan8/capstone2022_1/blob/main/pictures/%EB%8C%80%ED%9A%8C%20%EC%82%AC%EC%A7%84.png)

# 작품 소개
 최근 들어 아이스크림 무인매장과, 편의점을 많이 보셨을것 입니다. 인건비 상승과 기술의 발전으로 24시간 무인매장이 늘어나고 있습니다. 하지만 이러한 매장들은 사람이 자주 오지 않는 밤에도, 불을 환하게 켜놓습니다. 저희는 이러한 것들이 큰 에너지 낭비라고 생각되었습니다.  
   
 저희는 이런 문제를 매장내에 있는 CCTV를 사용해서 개선하고자 합니다. 무인 매장에는 보안, 도난 위험이 크기 때문에 CCTV를 많이 사용합니다. CCTV 영상에 사람이 있다는 것은 매장 주변에 사람이 있다는것을 의미합니다. 이를 object detection 기술을 통해, 사람이 있는지 없는지 판별하여 DB에 기록합니다.  
   
 매장내 조명은 사람의 유무정보를 읽어와서, 조명의 밝기를 조절합니다. 사람이 많은 시간에는 항상 켜놓고, 사람이 많이 없는 시간대에는 2가지 모드가 존재합니다. 첫번 째 절전모드는 매장 주변에 사람이 없을때 작동합니다. 이때에는 최소한의 전력을 이용하지만, 멀리에서 가게를 봤을때에는 열려있는 것 처럼 보이도록 조명을 최대한 활용합니다. 두번 째 ON모드는 CCTV에 사람이 탐지 되었을때 사용됩니다. 매장은 평상시대로 켜지게 되며 매장을 이용할 수 있도록 합니다. 에너지 절약 뿐만 아니라 사람이 가까이왔을 때 환해 지기 떄문에 시선을 끄는 효과를 받을 수도 있습니다.  
   
 이를 제어 할 수 있는 시스템은 10W의 정도의 전력 소비를합니다. 그리고 원래 CCTV를 관리하는 컴퓨터에 적용하면, 추가적인 비용없이도 제어가 가능할 것입니다. 매장설비를 다 뜯을 필요없이, 그기능을 하는 전구를 쓰거나 벽에있는 스위치에 장치를 달아도 쓸 수 있습니다. 비록 1,2개의 매장에서는 효과가 미미할것이라 생각하지만, 많은 가게들에 적용되면, 에너지 절약에 큰 효과가 있을 것이라 생각이됩니다.  
  
## 작품 요약 포스터
![작품 요약 포스터](https://github.com/uichan8/capstone2022_1/blob/main/pictures/%EC%BA%A1%EC%8A%A4%ED%86%A4_%ED%8F%AC%EC%8A%A4%ED%84%B0.jpg)
 

# 개발환경
Device
- Raspberry Pi 4 model B+ (4GB,8GB)
- Intel Neural Compute Stick 2
- usb 2.0 camera

OS
- Raspbian 10 Buster, 32-bit

Util
- openvino == 2021.4.2 (with openCV)
- cmake == 3.16.3

Python
- python == 3.7.3

# 사용법
## 라즈베리파이 초기 설정
### CCTV 기기   
1. Raspbian Buster, 32-bit OS를 설치합니다. [Pimager](https://www.raspberrypi.com/software/)
2. 라즈베리파이에 OpenVINO toolkit을 설치합니다. [모든 버전](https://storage.openvinotoolkit.org/repositories/openvino/packages/)
    1. tem 경로로 이동 합니다.  
    ```shell
    cd /tmp
    ```
    2. 빌드된 openvino 파일 다운로드 합니다.
    ```shell
    wget https://storage.openvinotoolkit.org/repositories/openvino/packages/2021.4.2/l_openvino_toolkit_runtime_raspbian_p_2021.4.752.tgz
    ```
    3. openvino 설치 경로 생성하고 받은 파일을 설치해줍니다.  
    ```shell
    sudo mkdir -p /opt/intel  
    cd /opt/intel  
    sudo tar -xf /tmp/l_openvino_toolkit_runtime_raspbian_p_2021.4.752.tgz -C /opt/intel  
    sudo mv l_openvino_toolkit_runtime_raspbian_p_2021.4.752 openvino  
    ```
    4. 다운로드 파일 삭제합니다.  
    ```shell
    rm -f /tmp/l_openvino_toolkit_runtime_raspbian_p_2021.4.752.tgz
    ```
    5. cmake를 설치합니다. 
    ```shell
    sudo apt install cmake
    ```
    6. openvino 환경 실행해줍니다.
    ```shell
    source /opt/intel/openvino/bin/setupvars.sh
    ```
    7. (optional) 터미널을 킬 때마다 위의 명령어를 실행하도록 하는 명령어 입니다.
    ```shell
    echo "source /opt/intel/openvino/bin/setupvars.sh" >> ~/.bashrc
    ```
    8. NCS2 규칙을 추가해 줍니다. `"$(whoami)"`에 계정이름으로 바꿔서 입력해주어야 합니다. (defult = pi)
    ```shell
    sudo usermod -a -G users "$(whoami)"
    sh /opt/intel/openvino/install_dependencies/install_NCS_udev_rules.sh
     ```
3. 기타 파일을 설치해줍니다
```shell
sudo apt install libgfortran5 libatlas3-base
sudo apt-get install libatlas-base-dev
```
4. 경로를 설정하고 git에서 코드를 클론해줍니다
```shell
git clone https://github.com/uichan8/capstone2022_1.git
```
5. requierments.txt를 설치해 줍니다.
```shell
pip3 install -r requierments.txt
```
### DB 기기
1. 경로를 설정하고 git에서 코드를 클론해줍니다
```shell
git clone https://github.com/uichan8/capstone2022_1.git
```
2. requierments.txt를 설치해 줍니다.
```shell
sudo pip3 install -r requierments.txt
```
3. Terminal 을 들어가서 DB 관련 프로그램 을 설치 해 줍니다.  
```shell
sudo apt install mariadb-server mariadb-client
```
4. Database 폴더안에 make_db를 참고하여 db를 생성해줍니다.

## 코드 실행
1. 먼저 공유기에 두 라즈베리파이의 고정 아이피를 잡아주고, `CCTV.py`안에 ip를 DB기기의 ip로 바꿔 줍니다.
2. 먼저 CCTV로 쓸 기기에 다음과 CCTV 객체탐지를 실행하는 명령어를 쳐 줍니다.
```shell
python3 CCTV.py
```
3. DB및 빛조절 DB를 담당할 기기에 조명에 조도를 조정해 줄 수 있는 실행합니다.
```shell
sudo python3 Lights.py
```
4. DB 기기에 감지 할 수 있는 센서들을 키는 명령어를 실행합니다.(optional)
```shell
sudo python3 sensor.py
```
5.DB 기기에 Ess 시스템을 가동하는 명령어를 실행합니다.(optional)
```shell
sudo python3 Ess.py
```
 
# TrobleShooting
1. 마리아 DB 원격접속 접근 거부 https://m.blog.naver.com/wlsdml1103/221159758141
2. DHT11 라즈베리파이 4 문제 https://stackoverflow.com/questions/63232072/cannot-import-name-beaglebone-black-driver-from-adafruit-dht
 
