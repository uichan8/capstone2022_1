from SensorUtils.DHT11 import DHT11
from DataBase.DB_manager import DB_manager
from datetime import datetime

def main():
    db = DB_manager(ip = '192.168.75.20')
    dht = DHT11(3)
    present_min = datetime.now().minute

    while True:
        if present_min != datetime.now().minute:
            present_min = datetime.now().minute
            
            #update Temperature and humidity
            temp = dht.getTemp()
            humi = dht.getHumi()
            db.update("temperture",temp)
            db.update("humidity",humi)

if __name__ == "__main__":
    main()
