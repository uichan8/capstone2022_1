from Led import Led
from Base import Base
import time

class Sign(Base):
    """간판"""
    main_led = [] # 항상 켜져있어야 하는 조명 = 중앙에 kookmin 에 붙어있는 조명
    sub_led  = [] # 사람 왔을 때 켜져있어야 하는 조명 = 주변 백라이트

    main_state = 0
    sub_state   = 0

    max_power =  12*12 #(W)

    def __init__(self,front:list,middle:list,back:list):
        for i in front:
            self.front_led.append(Led(i))
        for i in middle:
            self.middle_led.append(Led(i))
        for i in back:
            self.back_led.append(Led(i))

    @staticmethod
    def led_list_on(list,pwm):
        for led in list:
            led.on(pwm)

    def change_ceilling_state(self,front,mid,back):
        for i in range(1,30):
            front_light = self.front_state + (front - self.front_state)/30*i
            mid_light = self.mid_state + (mid - self.mid_state)/30*i
            back_light = self.back_state + (back - self.back_state)/30*i
            self.led_list_on(self.front_led,int(front_light))
            self.led_list_on(self.middle_led,int(mid_light))
            self.led_list_on(self.back_led,int(back_light))
            time.sleep(0.1)
        self.led_list_on(self.front_led,int(front))
        self.led_list_on(self.middle_led,int(mid))
        self.led_list_on(self.back_led,int(back))
        self.front_state = front
        self.mid_state = mid
        self.back_state = back
    
    def eco_mode(self):
        self.change_ceilling_state(100,40,10)
    
    def on_mode(self):
        self.change_ceilling_state(100,100,100)
    
    def off_mode(self):
        self.change_ceilling_state(0,0,0)

    def check_power(self):
        return (self.front_state + self.mid_state + self.back_led) / 300 * self.max_power #대충한거라 나중에 수정해야함
