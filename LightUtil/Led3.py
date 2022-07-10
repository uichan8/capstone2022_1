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
    
    def __init__(self,pin_num):
        self.led3_pin = 18
        self.color_array = list(np.zeros((10,3)))
    
    @staticmethod
    def clipping(Brightness):
        if(0 > Brightness):
            Brightness = 0
        if(Brightness > 255):
            Brightness = 255
        return Brightness

    
    def set_color(self, color, number):
        """
        led를 킬때 쓰는 메소드 입니다.
            input :
                Brightness(int) : 설정 할 밝기 (0 ~ 100) 을 입력합니다. default = 255
        """
        self.color_array[number] = [self.clipping(color[0]) ,self.clipping(color[1]) ,self.clipping(color[2])]
    
    def on(self, brightness = 100):
        for i in range(3,0,-1):
            pixel = neopixel.NeoPixel(board.D18,i)
            pixel.fill(np.array(self.color_array[i])*brightness/100)
        pixel.show()
       
    def off(self, led3num=0):
        """
        led를 끌때 쓰는 메소드 입니다.
        """
        self.on(0)
        
    def value(self,num=0):
        self.led3.fill(np.array([Brightness_r, Brightness_g, Brightness_b])*num)
        
if __name__ == '__main__':
    a = Led3(1)
    a.set_color([255,0,0],1)
    a.on()

    