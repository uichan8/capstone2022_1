import RPi.GPIO as GPIO
import board
import neopixel
import numpy as np

class Led3:
    """
    3색 led 의 밝기를 조절하는 메소드 입니다.
        input :
            led3_num(int)   : 3색 led pin 번호
            number(int)     : 3색 led의 갯수
    """
    led = None
    numofpixels = 0
    
    def __init__(self):
        self.led3_pin = 18
        self.color_array = list(np.zeros((10,3)))
    
    @staticmethod
    def clipping(Brightness):
        if(0 > Brightness):
            Brightness = 0
        if(Brightness > 255):
            Brightness = 255
        return Brightness

    
    def set_color(self,r , g ,b, number):
        """
        led를 킬때 쓰는 메소드 입니다.
            input :
                Brightness(int) : 설정 할 밝기 (0 ~ 100) 을 입력합니다. default = 255
        """
        self.color_array[number] = [self.clipping(r) ,self.clipping(g) ,self.clipping(b)]
    
    def on(self, brightness):
        for i in range(9,0,-1):
            pixel = neopixel.NeoPixel(board.D18,i)
            pixel.fill(self.color_array[i])
        pixel.show()
       
    def off(self, led3num=0):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        self.led3.fill[0, 0, 0]
        self.led3.show()
        
    def value(self,num=0):
        self.led3.fill(np.array([Brightness_r, Brightness_g, Brightness_b])*num)

    