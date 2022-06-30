import RPi.GPIO as GPIO
import neopixel

class Led3:
    """
    3색 led 의 밝기를 조절하는 메소드 입니다.

        input :
            led3_num(int)   : 3색 led pin 번호
            number(int)     : 3색 led의 갯수
    """
    led = None
    numofpixels = 0
    

    def __init__(self, led3_num, number=15):
        self.led3_pin = led3_num
        self.numofpixels = number
        self.led3 = neopixel.NeoPixel(self.led3_pin,self.numofpixels, auto_write = False)



    def on(self,led3num =0,Brightness_r = 255, Brightness_g = 255, Brightness_b = 255):
        """
        led를 킬때 쓰는 메소드 입니다.

            input :
                Brightness(int) : 설정 할 밝기 (0 ~ 100) 을 입력합니다. default = 255
        """
        if(0 > Brightness_r):
            Brightness_r = 0
        if(Brightness_r > 255):
            Brightness_r = 255

        if(0 > Brightness_g):
            Brightness_g = 0
        if(Brightness_g > 255):
            Brightness_g = 255

        if(0 > Brightness_b):
            Brightness_b = 0
        if(Brightness_b > 255):
            Brightness_b = 255
        self.led3[led3num] = (Brightness_r, Brightness_g, Brightness_b)
       

    def off(self, led3num=0):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        self.led3[led3num] = (0, 0, 0)