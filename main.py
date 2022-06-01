from time import *

#object class
from turtle import st
from LightUtil.Ceilling import Ceilling
from LightUtil.Sign import Sign

#database class
from DataBase.DB_manager import DB_manager

class user_time:
    start = 0
    finish = 0

    @staticmethod
    def is_time(time):
        return 0 <= time and time <= 24
    
    def __init__(self,start = 18,finish = 6):
        self.set_time(start,finish)

    def set_time(self,start,finish):
        """절전모드를 몇시부터 몇시까지로 설정할지를 설정해주는 메소드입니다. 시작 시간과 끝 시간이 같으면 항상 eco모드가 꺼지게 됩니다."""
        if not(self.is_time(start) and self.is_time(finish)):
            return
        self.start  = start
        self.finish = finish

        self.start = start
        self.finish = finish
        print(f"시작 시간 : {self.start} 끝 시간 : {self.finish} 으로 설정 완료 되었습니다.")

    def is_eco_time(self):
        hour = localtime(time()).tm_hour
        if self.start < self.finish:
            return self.start <= hour and hour < self.finish
        else:
            return self.start <= hour or hour < self.finish

def main():
    ceilling = Ceilling([18],[23],[24])
    sign     = Sign([16],[20])
    objects = [ceilling, sign]

    set_time = user_time()

    db = DB_manager()

    #속성(휘발성)
    switch = "off" #사용자가 강제로 조정하는 
    mode = "off" #매장 내 조명 on/off/eco(절전)
    in_store = False #가게 안에 사람이 있을경우 True 없을경우 False
    out_store = False #가게 밖에 사람이 있을경우 True 없을경우 False
    lx_in = 0 #매장 안 광도
    lx_out = 0 #매장 밖 광도
    tem = 0 # 온도
    humi = 0 # 습도

    while True:
        #update db from sensor
        #DHT11 code later
        #lumi sensor later

        #상태 업데이트

        #상태 판별

        #기기제어
        if   mode == 'on':
            [object.on_mode() for object in objects]
        elif mode == 'off':
            [object.off_mode() for object in objects]
        elif mode == 'eco':
            [object.eco_mode() for object in objects]

        print(mode)

if __name__ == "__main__":
    main()

