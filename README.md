# capstone2022_1
# 요약
2022년 1학기 정일엽 교수님 캡스톤 디자인 수업 'light24'조의 코드 파일입니다.  
CCTV로부터 받아온 영상 정보로부터 object detection(YOLOX_tiny)를 시행하여 사람이 있는지 없는지를 탐지하고, 매장 내의 조명을 조절하여 에너지를 관리하는 프로젝트입니다
# 작품 소개

# 개발환경
Device
- Raspberry Pi 4 model B+ (4GB,8GB)
- Intel Neural Compute Stick 2
- usb2.0 camera

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
pip3 install -r requierments.txt
```
3. Terminal 을 들어가서 DB 관련 프로그램 을 설치 해 줍니다.  
```shell
sudo apt install mariadb-server mariadb-client
```
4. Database 폴더안에 make_db를 참고하여 db를 생성해줍니다.
## 코드 실행
1. 같은 공유기에 DB기기에는 192.168.75.20 CCTV기기는 192.168.75.21 로 고정시킵니다. (코드 내에서 ip변경 가능 및 추후에 args로 넣을수 있도록 수정 예정)
2. 먼저 CCTV로 쓸 기기에 `CCTV.py` 를 실행합니다.
3. DB및 빛조절 DB를 담당할 기기에 `Lights.py` 를 실행합니다.
 
# TrobleShooting
1. 마리아 DB 원격접속 접근 거부 https://m.blog.naver.com/wlsdml1103/221159758141
