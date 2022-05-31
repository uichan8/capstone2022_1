from abc import ABC,abstractmethod #추상클래스 관련 클래스

class Base(ABC):
    """모든 기기가 가져야할 정보를 업데이트 해주고, 필수적으로 들어가야할 메소드를 정의합니다."""
    #속성(휘발성)
    switch = "off" #사용자가 강제로 조정하는 
    mode = "off" #매장 내 조명 on/off/eco(절전)
    in_store = False #가게 안에 사람이 있을경우 True 없을경우 False
    out_store = False #가게 밖에 사람이 있을경우 True 없을경우 False
    lx = 0 #광도
    tem = 0 # 온도

    #속성(저장성)
    start_time = None #절전모드 시작 시간
    finish_time = None #절전모드 끝 시간

    #기본 메소드
    def __init__(self):
        #DB에서 저장성 값을 입력합니다.
        pass

    def update_mode(self) -> bool:
        #설정 시간 밖일경우 -> off
        #아무데도 사람 없을 경우 -> off
        #밖에 사람이 있을 경우 -> eco
        #안에 사람이 있을 경우 -> on
        pass

    def update_store_state(self) -> bool:
        """매장상태를(광도,온도,사람) 업데이트 해주는 메소드 입니다."""
        #DB에서 읽어와서 값을 저장 업데이트 성공시 true 출력
        #업데이트 후 mode 업데이트 실시
        return True
    
    def set_time(self,start,finish):
        """절전모드를 몇시부터 몇시까지로 설정할지를 설정해주는 메소드입니다."""
        #if(!시간 형식 맞는가?):
        #   print("시간 형식은 #### 이여야 합니다.")
        #   return
        self.start_time = start
        self.finish_time = finish
        print(f"시작 시간 : {self.start_time} 끝 시간 : {self.finish_time} 으로 설정 완료 되었습니다.")

    @abstractmethod
    def on_mode():
        """전원을 켜야할 때 해야되는 메소드 입니다. 꼭 오버라이딩 하세요"""
        pass

    @abstractmethod
    def off_mode():
        """전원을 꺼야 할 때 해야되는 메소드 입니다. 꼭 오버라이딩 하세요"""
        pass
    
    @abstractmethod
    def eco_mode():
        """절전 모드일 때 시행되는 메소드입니다. 꼭 오버라이딩 하세요"""
        pass

    @abstractmethod
    def check_power() -> int:
        """전력량을 확인하는 메소드입니다. 꼭 오버라이딩 하세요"""
        pass