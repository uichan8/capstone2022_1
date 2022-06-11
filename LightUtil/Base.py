from abc import ABC,abstractmethod #추상클래스 관련 클래스

class Base(ABC):
    """모든 기기가 가져야할 정보를 업데이트 해주고, 필수적으로 들어가야할 메소드를 정의합니다."""

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