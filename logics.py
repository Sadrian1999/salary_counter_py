from data import Data

class Logics:
    def __init__(self) -> None:
        self.age: int
        self.wage: int
        self.paid_off: int
        self.sick: int
        self.datas = []
        self.workdays = []
        self.total_base = 0
        self.total_thirty = 0   
        self.total_fourty = 0
        self.total_hundred = 0
        self.tax = 0
        self.tb = 0
        self.brutto_money = 0
        self.nett_money = 0
        self.money_care = 200
        self.is_vem: bool
        
    def convert_to_decimal(self, time: str):
        time = time.split(':')
        return float(int(time[0]) + int(time[1]) / 60)
    
    def break_time(self, worked_hours: float):
        if self.is_vem:
            if worked_hours > 9 + 1/ 3:
                return 1
            elif worked_hours <= 6:
                return 0
            else:
                return 0.5
        elif self.age > 18:
            if worked_hours <= 6: return 0
            if worked_hours > 6 and worked_hours <= 9 + 1 / 3: return 1 / 3
            if worked_hours > 9 + 1 / 3 and worked_hours <= 12.75: return 0.75
        else:
            if worked_hours <= 4.5: return 0
            if worked_hours > 4.5 and worked_hours <= 6: return 0.5
            if worked_hours > 6 and worked_hours <= 8.75: return 0.75
            
    def counting_hours(self, clk_in: float, clk_out: float, is_double_money: bool, date: str):
        data = Data()
        data.day = date
        self.workdays.append(date)
        
        if clk_in < clk_out:
            hours = clk_out - clk_in
            if hours > 12.75 or hours < 4:
                raise ValueError()
            double_money = 1
            
            if is_double_money:
                double_money = 2
                data.hundred_percent += hours - self.break_time(hours)
            if not is_double_money:
                data.base_hours += hours - self.break_time(hours)
            if clk_in > 0 and clk_out <= 6:
                data.fourty_percent += hours * double_money
    
            elif clk_in > 22 and clk_out <= 24:
                data.fourty_percent += hours * double_money
                
            elif clk_in > 18 and clk_out <= 22:
                data.thirty_percent += hours * double_money
                
            elif clk_in > 0 and clk_in < 6 and clk_out <= 18 and clk_out > 6:
                data.fourty_percent += (6 - clk_in) * double_money
                
            elif clk_in > 6 and clk_out <= 22 and clk_out > 18:
                data.thirty_percent += (clk_out - 18) * double_money
            
            elif clk_in > 18 and clk_out <= 24 and clk_out > 22:
                data.fourty_percent += (24 - clk_out) * double_money
                data.thirty_percent += (4 - (clk_in - 18)) * double_money
            
            elif clk_in > 0 and clk_in <= 6 and clk_out < 22 and clk_out >= 18:
                data.fourty_percent += (24 - clk_out) * double_money
                data.thirty_percent += (clk_out - 18) * double_money
            
            elif clk_in > 6 and clk_in <= 18 and clk_out <= 24 and clk_out > 22:
                data.fourty_percent += (clk_out - 22) * double_money
                data.thirty_percent += 4 * double_money
                    
            self.total_base += data.base_hours 
            self.total_thirty += data.thirty_percent
            self.total_fourty += data.fourty_percent
            self.total_hundred += data.hundred_percent
            
            self.datas.append(data)
    
    def counting_money(self):
        self.brutto_money += self.total_base * self.wage + self.total_thirty * self.wage * 0.3 + self.total_fourty * self.wage * 0.4 + self.total_hundred * self.wage
        self.brutto_money += self.sick * self.wage * 0.7 + self.paid_off * self.wage
      
        if self.age < 25:
            if self.brutto_money > 433_000:
                self.tax = (self.brutto_money - 433_000) * 0.15
        
        if self.age >= 25:
            self.tax = self.brutto_money * 0.15
        self.tb = self.brutto_money * 0.185
        self.nett_money = self.brutto_money - self.tax + self.money_care
    
"""l = Logics()
l.age = 23
l.wage = 1000
l.sick = 0
l.paid_off = 0
l.counting_hours(14, 23, False, "2023.01.01.")
l.counting_hours(14, 23, False, "2023.01.02.")
l.counting_money()
print(l.brutto_money, l.nett_money)"""