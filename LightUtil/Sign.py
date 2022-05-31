from Led import Led
from Base import Base
import time

class Sign(Base):
    """간판"""
    main_led = [] # 항상 켜져있어야 하는 조명 = 중앙에 kookmin 에 붙어있는 조명
    sub_led  = [] # 사람 왔을 때 켜져있어야 하는 조명 = 주변 백라이트

    main_state = 0
    sub_state  = 0

    max_power =  12*23 #(W)

    def __init__(self,main:list,sub:list):
        for i in main:
            self.main_led.append(Led(i))
        for i in sub:
            self.sub_led.append(Led(i))

    @staticmethod
    def led_list_on(list,pwm):
        for led in list:
            led.on(pwm)

    def change_ceilling_state(self,main,mid):
        for i in range(1,30):
            main_light = self.main_state + (main - self.main_state)/30*i
            mid_light  = self.mid_state + (mid - self.mid_state)/30*i
            self.led_list_on(self.main_led,int(main_light))
            self.led_list_on(self.sub_led,int(mid_light))
            time.sleep(0.1)
        self.led_list_on(self.main_led,int(main))
        self.led_list_on(self.sub_led,int(mid))

        self.main_state = main
        self.mid_state = mid
    
    def eco_mode(self):
        self.change_ceilling_state(100,40)
    
    def on_mode(self):
        self.change_ceilling_state(100,100)
    
    def off_mode(self):
        self.change_ceilling_state(0,0)

    def check_power(self):
        return (self.main_state + self.mid_state) / 300 * self.max_power #대충한거라 나중에 수정해야함
