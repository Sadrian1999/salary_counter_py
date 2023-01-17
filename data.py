class Data:
    def __init__(self,day=None, base=0, thirty=0, fourty=0, hundred=0, plus=0):
        self.day = day,
        self.base_hours = base
        self.thirty_percent = thirty
        self.fourty_percent = fourty
        self.hundred_percent = hundred
        self.plus_hours = plus
    
    def __str__(self) -> str:
        return f"{self.day} {self.base_hours:.2f} {self.thirty_percent:.2f} {self.fourty_percent:.2f} {self.hundred_percent:.2f}"