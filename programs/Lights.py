from time import *
from Utils.User_time_set import User_time_set

#object class
from LightUtil.Ceilling import Ceilling
from LightUtil.Sign import Sign
from Utils.Switch import Switch

#database class
from DataBase.DB_manager import DB_manager

def main():
    #setup DB
    db = DB_manager()

    #output objects
    ceilling = Ceilling([18],[23],[25])
    sign     = Sign([16],[20])
    objects = [ceilling, sign]

    #input objects
    on_off_switch = Switch(13)
    pri_eco_switch = Switch(19) #this is for presentation

    #settings
    set_time = User_time_set(0,0) #시작시간 종료시간 설정

    #속성(휘발성)
    mode = "off" #매장 내 조명 on/off/eco(절전)
    out_store = False 

    while True:
        #상태 업데이트
        on_off_switch.update()
        pri_eco_switch.update()
        out_store = db.read_last("camera")
        print(out_store)#llllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll
        out_store = int(out_store)
        print(f"eco time : {set_time.is_eco_time()}")
        print(f"cam : {out_store}")

        #상태 판별
        if not on_off_switch.state:
            mode = 'off'
        elif   pri_eco_switch.state or (set_time.is_eco_time() and on_off_switch.state and not out_store):
            mode = 'eco'
        else:
            mode = 'on'

        #기기제어
        if   mode == 'on':
            [object.on_mode() for object in objects]
        elif mode == 'off':
            [object.off_mode() for object in objects]
        elif mode == 'eco':
            [object.eco_mode() for object in objects]

        print(f"mode : {mode}")
        print("----------------------------")

if __name__ == "__main__":
    main()

