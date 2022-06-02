import RPi.GPIO as GPIO

class Switch():
    """토글 스위치에 대한 코드입니다."""
    _pin_num = 0
    state = False

    def __init__(self,pin_num):
        self._pin_num = pin_num
        GPIO.setwarnings(False) #IMPORTANT
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._pin_num, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
        self.state = True if GPIO.input(self._pin_num) == GPIO.HIGH else False
        
    def update(self):
        self.state = True if GPIO.input(self._pin_num) == GPIO.HIGH else False

    @property
    def state(self):
        return self.state

