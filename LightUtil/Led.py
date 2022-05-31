import RPi.GPIO as GPIO

class Led:
    led = None
    pin_num = 0

    def __init__(self, led_num, frequency = 50):

        self.pin_num = led_num
        GPIO.setwarnings(False) #IMPORTANT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.led = GPIO.PWM(self.pin_num, frequency)
        self.led.start(0)

    def on(self,Brightness = 100):
        if(0 > Brightness):
            Brightness = 0
        if(Brightness > 100):
            Brightness = 100
        self.led.ChangeDutyCycle(Brightness)



    def off(self):
        self.led.ChangeDutyCycle(0)