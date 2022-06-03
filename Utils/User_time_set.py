from time import *

class User_time_set:
    start = 0
    finish = 0

    @staticmethod
    def is_time(time):
        return 0 <= time and time <= 24
    
    def __init__(self,start = 18,finish = 6):
        self.set_time(start,finish)

    def set_time(self,start,finish):
        """절전모드를 몇시부터 몇시까지로 설정할지를 설정해주는 메소드입니다. 시작 시간과 끝 시간이 같으면 항상 eco모드가 꺼지게 됩니다."""
        if not(self.is_time(start) and self.is_time(finish)):
            return
        self.start  = start
        self.finish = finish

        self.start = start
        self.finish = finish
        print(f"시작 시간 : {self.start} 끝 시간 : {self.finish} 으로 설정 완료 되었습니다.")

    def is_eco_time(self):
        hour = localtime(time()).tm_hour
        if self.start < self.finish:
            return self.start <= hour and hour < self.finish
        else:
            return self.start <= hour or hour < self.finish