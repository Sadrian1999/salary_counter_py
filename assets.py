
class User():
    def __init__(self, wage=None, age=None, position=None, application_type=None, job_time=None, tax_free=None, is_vem=None) -> None:
        self.wage = wage
        self.age = age
        self.position = position
        self.application_type = application_type
        self.job_time = job_time
        self.tax_free = tax_free
        
    def read_data(self) -> list:
        with open("user_data.txt", "rt") as file:
            lines = file.readlines()
        self.wage = int(lines[0].rstrip("\n"))
        self.age = int(lines[1].rstrip("\n"))
        self.is_vem = True if lines[2].rstrip("\n") == "VÉM" else False
        self.application_type = lines[3].rstrip("\n")
        self.job_time = lines[3].rstrip("\n")
        self.tax_free = lines[3].rstrip("\n")
        

class Blocking():
    def __init__(self, clk_in=None, clk_out=None) -> None:
        self.clk_in = clk_in
        self.clk_out = clk_out
    
    def __repr__(self) -> str:
        return f"{self.clk_in} - {self.clk_out}"


class Hours:
    def __init__(self, base=0, thirty=0, fourty=0, hundred=0, plus=0):
        self.base_hours = base
        self.thirty_percent = thirty
        self.fourty_percent = fourty
        self.hundred_percent = hundred
        self.plus_hours = plus
        
    def __str__(self) -> str:
        return f"{self.base_hours} {self.thirty_percent} {self.fourty_percent} {self.hundred_percent}"
        
        
class Day():
    def __init__(self, blockings=[Blocking], is_holiday=False, is_sick=False, is_paid=False) -> None:
        self.blockings = blockings
        self.is_holiday = is_holiday
        self.is_sick = is_sick
        self.is_paid = is_paid