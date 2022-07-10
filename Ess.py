from Utils.Relay import Relay
from DataBase import  DB_manager
from Utils.Battery import Battery

while True:
    db = DB_manager()
    battery = Battery()
    relay = Relay(26)
    charge = True
    discharge = True
    device_list = ["camera", "light"]
    
    #에너지 사용량 취합
    power = 0
    for device in device_list:
        db.read_last(device)
        power += int(db.read_last(device)[1])
        
    #베터리 상태 업데이트
    #베터리 보호
    if battery.return_level() < 20:
        discharge = False
    if battery.return_level() > 80:
        charge = False

    #일정 전압 유지
    if power >= 20:
        charge = False
    else:
        charge = True

    if power <= 20:
        discharge = False
    else:
        discharge = True

    #전압 제어
    if charge:
        relay.on()
        battery.charge()
    else:
        relay.off()

    if discharge:
        battery.discharge()



