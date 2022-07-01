import RPi.GPIO as GPIO

class Led3:
    """
    led 의 밝기를 조절하는 메소드 입니다.

        input :
            led_num(int)   : led pin 번호
            frequency(int) : led 의 주파수를 설정합니다. default = 100
    """
    led = None
    pin_num = 0

    def __init__(self, led_num,color = [256,256,256], frequency = 100):
        self.pin_num = led_num
        GPIO.setwarnings(False) #IMPORTANT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.pin_num, GPIO.OUT)
        self.led = GPIO.PWM(self.pin_num, frequency)
        self.led.start(0)
        self.color = color

    def on(self,Brightness = 100):
        """
        led를 킬때 쓰는 메소드 입니다.

            input :
                Brightness(int) : 설정 할 밝기 (0 ~ 100) 을 입력합니다. default = 100
        """
        #3색 led를 키는 코드

    def off(self):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        #색 led를 끄는 코드