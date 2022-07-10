from time import *
from Utils.User_time_set import User_time_set

#object class
from LightUtil.Ceilling import Ceilling
from LightUtil.Sign import Sign
from Utils.Switch import Switch

#database class
from DataBase.DB_manager import DB_manager

def main():
    #output objects
    ceilling = Ceilling([21],[20],[16])
    sign     = Sign([18],[12])
    objects = [ceilling, sign]

    #input objects
    on_off_switch = Switch(17)
    pri_eco_switch = Switch(27) #this is for presentation

    #settings
    set_time = User_time_set(0,0) #시작시간 종료시간 설정

    #속성(휘발성)
    mode = "off" #매장 내 조명 on/off/eco(절전)
    out_store = False
    past_mode = None

    while True:
        #상태 업데이트
        db = DB_manager()
        on_off_switch.update()
        pri_eco_switch.update()
        out_store = db.read_last("camera")
        outstore = bool(int(out_store[1]))
        print(f"data     : {out_store[1]}")
        print(f"eco time : {set_time.is_eco_time()}")
        print(f"cam      : {outstore}")
        print(f"pri eco  : {pri_eco_switch.state}")
        print(f"on off   : {on_off_switch.state}")
        print((set_time.is_eco_time() and on_off_switch.state and not out_store[1]))

        #상태 판별
        if not on_off_switch.state:
            mode = 'off'
        elif   pri_eco_switch.state or (set_time.is_eco_time() and on_off_switch.state and not outstore):
            mode = 'eco'
        else:
            mode = 'on'

        #기기제어
        if past_mode != mode:
            if   mode == 'on':
                [object.on_mode() for object in objects]
            elif mode == 'off':
                [object.off_mode() for object in objects]
            elif mode == 'eco':
                [object.eco_mode() for object in objects]
                
        past_mode = mode
    

        print(f"mode : {mode}")
        print("----------------------------")

if __name__ == "__main__":
    main()

