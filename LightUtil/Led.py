import RPi.GPIO as GPIO

class Led:
    """
    led 의 밝기를 조절하는 메소드 입니다.

        input :
            led_num(int)   : led pin 번호
            frequency(int) : led 의 주파수를 설정합니다. default = 100
    """
    led = None
    pin_num = 0

    def __init__(self, led_num, frequency = 200):
        self.pin_num = led_num
        GPIO.setwarnings(False) #IMPORTANT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.led = GPIO.PWM(self.pin_num, frequency)
        self.led.start(0)

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
        self.led.ChangeDutyCycle(Brightness)

    def off(self):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        self.led.ChangeDutyCycle(0)