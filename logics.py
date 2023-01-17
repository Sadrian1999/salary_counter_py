class Logics:
    def __init__(self) -> None:
        self.age: int
        self.base_hours = []
        self.thirty_percent = []
        self.fourty_percent = []
        self.wage: int
        self.paid_off: int
        self.sick: int
        self.hundred_percent = []
        self.plus_hours = []
        self.date = []
        
    def convert_to_decimal(self, time: str):
        time = time.split(':')
        return float(int(time[0]) + int(time[1]) / 60)
    
    def break_time(self, worked_hours: float):
        if self.age > 18:
            if worked_hours <= 6: return 0
            if worked_hours > 6 and worked_hours <= 9 + 1 / 3: return 1 / 3
            if worked_hours > 9 + 1 / 3 and worked_hours <= 12.75: return 0.75
        else:
            if worked_hours <= 4.5: return 0
            if worked_hours > 4.5 and worked_hours <= 6: return 0.5
            if worked_hours > 6 and worked_hours <= 8.75: return 0.75
            
    def counting_hours(self, clk_in: float, clk_out: float, is_double_money: bool):
        if clk_in < clk_out:
            hours = clk_out - clk_in
            double_money = 1
            
            if is_double_money:
                double_money = 2
                self.hundred_percent.append(hours)
                
            if clk_in > 0 and clk_out <= 6:
                self.fourty_percent.append(hours * double_money)
                self.thirty_percent.append(0)
    
            elif clk_in > 22 and clk_out <= 24:
                self.fourty_percent.append(hours * double_money)
                self.thirty_percent.append(0)
                
            elif clk_in > 18 and clk_out <= 22:
                self.thirty_percent.append(hours * double_money)
                self.fourty_percent.append(0)
                
            elif clk_in > 0 and clk_in < 6 and clk_out <= 18 and clk_out > 6:
                self.fourty_percent.append((6 - clk_in) * double_money)
                self.thirty_percent.append(0)
                
            elif clk_in > 6 and clk_out <= 22 and clk_out > 18:
                self.thirty_percent.append((clk_out - 18) * double_money)
                self.fourty_percent.append(0)
            
            elif clk_in > 18 and (clk_out <= 24 or clk_out == 0) and clk_out > 22:
                self.fourty_percent.append((6 - clk_in) * double_money)
                self.thirty_percent.append((clk_out - 18) * double_money)
            
            elif clk_in > 0 and clk_in <= 6 and clk_out < 22 and clk_out >= 18:
                self.fourty_percent.append((6 - clk_in) * double_money)
                self.thirty_percent.append((clk_out - 18) * double_money)
            
            elif clk_in > 6 and clk_in <= 18 and (clk_out <= 24 or clk_out == 0) and clk_out > 22:
                self.fourty_percent.append((clk_out - 22) * double_money)
                self.thirty_percent.append(4 * double_money)
            else:
                self.thirty_percent.append(0)
                self.fourty_percent.append(0)
            self.base_hours.append(hours - self.break_time(hours))
            if not is_double_money:
                self.hundred_percent.append(0)
    
    def counting_money(self):
        self.brutto_money = 0
        nett_money = 0
        tax = 0
        tb: float
        money_care = 200
        self.brutto_money += sum(self.base_hours) * self.wage
        self.brutto_money += sum(self.thirty_percent) * self.wage * 0.3
        self.brutto_money += sum(self.fourty_percent) * self.wage * 0.4
        self.brutto_money += self.sick * self.wage * 0.7
        self.brutto_money += self.paid_off * self.wage
        self.brutto_money += sum(self.hundred_percent) * self.wage
        
        if self.age < 25:
            if self.brutto_money > 433_000:
                tax = (self.brutto_money - 433_000) * 0.15
        
        if self.age >= 25:
            tax = self.brutto_money * 0.15
        tb = self.brutto_money * 0.185
        nett_money = self.brutto_money - tax
        return nett_money