#test
import RPi.GPIO as GPIO


class Ess:

    def __init__(self,fb_pin, onoff_pin ):
        self.Feedbackpin = fb_pin
        self.onoffpin = onoff_pin
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.Feedbackpin, GPIO.OUT)
        GPIO.setup(self.onoffpin, GPIO.OUT)
        


    def Charge(self):
        GPIO.output(self.onoffpin, True)
        



    def Discharge(self):
        GPIO.output(self.onoffpin, False)