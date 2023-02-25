from assets import Hours, Blocking

class Logics:
    def __init__(self, age=0, is_vem=False) -> None:
        self.age = age
        self.is_vem = is_vem
    
    def break_time(self, worked_hours: float):
        if self.is_vem:
            if worked_hours > 9 + 1/ 3:
                return 1
            elif worked_hours <= 6:
                return 0
            else:
                return 0.5
        elif self.age >= 18:
            if worked_hours <= 6: return 0
            if worked_hours > 6 and worked_hours <= 9 + 1 / 3: return 1 / 3
            if worked_hours > 9 + 1 / 3 and worked_hours <= 12.75: return 0.75
        else:
            if worked_hours <= 4.5: return 0
            if worked_hours > 4.5 and worked_hours <= 6: return 0.5
            if worked_hours > 6 and worked_hours <= 8.75: return 0.75
            
    def counting_hours(self, blocking: Blocking, is_double_money: bool) -> Hours:
        
        total_hours = Hours()
        hundred_percent = 0
        thirty_percent = 0
        fourty_percent = 0
        base_hours = 0
        double_money = 1
        clk_in = blocking.clk_in
        clk_out = blocking.clk_out
        
        if clk_in < clk_out:
            hours = clk_out - clk_in

            if is_double_money:
                double_money = 2
                hundred_percent += hours - self.break_time(hours)
                
            if not is_double_money:
                base_hours += hours - self.break_time(hours)
                
            if hours > 12.75 or hours < 4:
                raise ValueError()
                
            if clk_in > 0 and clk_in < 6 and clk_out <= 18 and clk_out > 6:
                fourty_percent += (6 - clk_in) * double_money
                
            elif clk_in > 6 and clk_out <= 22 and clk_out > 18:
                thirty_percent += (clk_out - 18) * double_money
            
            elif clk_in > 18 and clk_out <= 24 and clk_out > 22:
                fourty_percent += (24 - clk_out) * double_money
                thirty_percent += (22 - clk_in - self.break_time(hours)) * double_money
            
            elif clk_in > 0 and clk_in <= 6 and clk_out < 22 and clk_out >= 18:
                fourty_percent += (24 - clk_out) * double_money
                thirty_percent += (clk_out - 18) * double_money
            
            elif clk_in > 6 and clk_in <= 18 and clk_out <= 24 and clk_out > 22:
                fourty_percent += (clk_out - 22) * double_money
                thirty_percent += 4 * double_money
        
        if clk_in > clk_out:
            hours = 24 - clk_in + clk_out
            
            if is_double_money:
                double_money = 2
                hundred_percent += hours - self.break_time(hours)
            
            if not is_double_money:
                base_hours += hours - self.break_time(hours)
                
            if hours > 12.75 or hours < 4:
                raise ValueError()
            
            if clk_in >= 22 and clk_out <= 6:
                fourty_percent += (hours - self.break_time(hours)) * double_money
            
            elif clk_in >= 18 and clk_out <= 6:
                fourty_percent += (2 + clk_out) * double_money
                thirty_percent += (22 - clk_in - self.break_time(hours)) * double_money
                
            elif clk_in >= 12 and clk_out >= 0:
                thirty_percent += 4 * double_money
                temp_clk_out = clk_out + 24
                fourty_percent += (temp_clk_out - 22) * double_money
            
        total_hours.base_hours = base_hours
        total_hours.fourty_percent = fourty_percent
        total_hours.thirty_percent = thirty_percent
        total_hours.hundred_percent = hundred_percent
        
        return total_hours  