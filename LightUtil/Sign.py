if __name__ == "__main__":
    from Led3 import *
    from Base import *
    from Led import *
else:
    from LightUtil.Led3 import *
    from LightUtil.Base import *
    from LightUtil.Led import *
import time

class Sign(Base):
    """간판의 조명을 조절하는 클래스 입니다.
        input : 
            main(list) : 간판 매인 조명의 조명의 입력 핀들의 번호들을 입력 합니다.(항상 켜져 있어야 하는 조명)
            sub(list)  : 간판 중간라인의 조명의 입력 핀들의 번호들을 입력 합니다.
        """
    main_led = [] # 항상 켜져있어야 하는 조명 = 중앙에 kookmin 에 붙어있는 조명
    sub_led  = [] # 사람 왔을 때 켜져있어야 하는 조명 = 주변 백라이트
    
    color1 = [0,255,15]
    color2 = [100,255,0]

    main_state = 0
    sub_state  = 0

    max_power =  12*23 #(W)

    def __init__(self,main:list,sub:list):
        for i in main:
            self.main_led.append(Led3(i))
        for i in sub:
            self.sub_led.append(Led(i))
            
        self.main_led[0].set_color(self.color1,1)
        self.main_led[0].set_color(self.color2,2)

    @staticmethod
    def led_list_on(list,pwm):
        for led in list:
            led.on(pwm)

    def change_ceilling_state(self,main,sub):
        for i in range(1,30):
            main_light = self.main_state + (main - self.main_state)/30*i
            sub_light  = self.sub_state + (sub - self.sub_state)/30*i
            self.led_list_on(self.main_led,int(main_light))
            self.led_list_on(self.sub_led,int(sub_light))
            time.sleep(0.01)
        self.led_list_on(self.main_led,int(main))
        self.led_list_on(self.sub_led,int(sub))

        self.main_state = main
        self.sub_state = sub
    
    def eco_mode(self):
        """매장 간판 조명을 절약하는 모드입니다."""
        self.change_ceilling_state(40,0)
    
    def on_mode(self):
        """매장 간판 조명을 켜는 모드입니다."""
        self.change_ceilling_state(100,100)
    
    def off_mode(self):
        """매장 간판 조명을 끌때 쓰는 메소드 입니다."""
        self.change_ceilling_state(0,0)

    def check_power(self):
        return (self.main_state + self.sub_state) / 300 * self.max_power #대충한거라 나중에 수정해야함 나중에 수정해야함
    
if __name__ == '__main__':
    a = Sign([18],[12])
    a.eco_mode()
    input()
    a.on_mode()
    input()
