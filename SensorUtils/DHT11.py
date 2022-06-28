import Adafruit_DHT

class DHT11:
    def __init__(self, dht_num):
        self.sensor = Adafruit_DHT.DHT11
        self.pin_num = dht_num

    def getTemp(self):
        _ , temp = Adafruit_DHT.read_retry(self.sensor, self.pin_num)
        return temp

    def getTemp(self):
        humi = Adafruit_DHT.read_retry(self.sensor, self.pin_num)
        return humi 