import RPi.GPIO as GPIO

class Relay():
    def __init__(self, pin_num):
        self.relay = pin_num
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.relay, GPIO.OUT)
        
    def on(self):
        GPIO.output(self.relay, GPIO.HIGH)
            
    def off(self):
        GPIO.output(self.relay, GPIO.LOW)
        
