from SensorUtils.DHT11 import DHT11
from DataBase.DB_manager import DB_manager
from datetime import datetime

def main():
    dht = DHT11(22)
    db = DB_manager()
    present_min = datetime.now().minute
    while True:
        if present_min != datetime.now().minute:
            #update Temperature and humidity
            try:
                humi,temp = dht.getTemp()
                db.update("temperture",temp)
                db.update("humidity",int(humi))
                print(f"temp : {temp}, humi : {humi} ")
            except RuntimeError as error:
                print("update fail please wait")
                continue
        present_min = datetime.now().minute

if __name__ == "__main__":
    main()
