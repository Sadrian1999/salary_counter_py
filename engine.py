from tkinter import messagebox
from assets import User, Blocking
from logics import Logics

class Engine():
    def __init__(self) -> None:
        self.instructions = {
            "save_settings": [],
            "workdays": [],
            "calculate": []
        }
        self.user = User()
        self.logics = Logics()
        self.days = {
            
        }
    
    def post(self, type: str, *args) -> None:
        for item in args:
            self.instructions[type].append(item)
    
    def get(self, type: str) -> list:
        return self.instructions[type]
    
    def save_settings(self) -> None:
        wage = self.instructions["save_settings"][0]
        age = self.instructions["save_settings"][1]
        position = self.instructions["save_settings"][2]
        application_type = self.instructions["save_settings"][3]
        job_time = self.instructions["save_settings"][4]
        tax_free = self.instructions["save_settings"][5]
        
        if application_type == "Diák":
            job_time = '-'
        try:
            int(wage)
        except Exception:
            return messagebox.showerror("Hiba", "Hibás órabér")
        
        try:
            int(age)
        except Exception:
            return messagebox.showerror("Hiba", "Hibás életkor")
        
        if int(wage) > 10000 or int(wage) < 1000:
            return messagebox.showerror("Hiba", "Hibás órabér")
        
        if int(age) > 99 or int(age) < 15:
            return messagebox.showerror("Hiba", "Hibás életkor")
        
        with open("user_data.txt", "wt") as file:
            for element in (wage, age, position, application_type, job_time, tax_free):
                file.write(str(element) + "\n")
                
        return messagebox.showinfo("Siker", "Adatok sikeresen mentve")
    
    def convert_to_decimal(self, time: str) -> float:
        time = time.split(':')
        return float(int(time[0]) + int(time[1]) / 60)
    
    def add_blocking(self, clk_in: str, clk_out: str, day: str) -> None:
        blocking = Blocking(clk_in, clk_out)
        self.instructions["workdays"].append(blocking)
    
e = Engine()
