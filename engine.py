from tkinter import messagebox

class Engine():
    def __init__(self) -> None:
        self.instructions = {
            "save_settings": [],
            "add_blocking": [],
            "calculate": []
        }
    
    def post(self, type: str, *args):
        for item in args:
            self.instructions[type].append(item)
    
    def get(self, type: str):
        return self.instructions[type]
    
    def save_settings(self):
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
    
    
e = Engine()
    
