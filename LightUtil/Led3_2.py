import RPi.GPIO as GPIO
import neopixel

class Led3:
    """
    led 의 밝기를 조절하는 메소드 입니다.

        input :
            led_num(int)   : led pin 번호
            frequency(int) : led 의 주파수를 설정합니다. default = 100
    """
    led = None
    pin_num = 0

    def __init__(self, led3_num, r, g, b,number=15,frequency = 100):
        self.pin_num = led3_num
        GPIO.setwarnings(False) #IMPORTANT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.led = GPIO.PWM(self.pin_num, frequency)
        self.led.start(0)
        self.numofpixels = number
        self.led3 = neopixel.NeoPixel(self.pin_num,self.numofpixels, auto_write = False)
        self.led3[led3_num] = (r, g, b)


    def on(self,Brightness = 100):
        """
        led를 킬때 쓰는 메소드 입니다.

            input :
                Brightness(int) : 설정 할 밝기 (0 ~ 100) 을 입력합니다. default = 100
        """
        if(0 > Brightness):
            Brightness = 0
        if(Brightness > 100):
            Brightness = 100
        self.led3.show()
        self.led3.ChangeDutyCycle(Brightness)


    def off(self):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        self.led.ChangeDutyCycle(0)
        self.led3.show()