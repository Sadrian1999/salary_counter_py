class Data:
    def __init__(self) -> None:
        self.day: str
        self.base_hours: float = 0
        self.thirty_percent: float = 0
        self.fourty_percent: float = 0
        self.hundred_percent: float = 0
        self.plus_hours: float = 0
        
    def add(self,day=None, base=0, thirty=0, fourty=0, hundred=0, plus=0):
        self.day = day,
        self.base_hours = base
        self.thirty_percent = thirty
        self.fourty_percent = fourty
        self.hundred_percent = hundred
        self.plus_hours = plus