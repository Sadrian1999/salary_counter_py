import tkinter as tk
from tkcalendar import Calendar
from tkinter import ttk, messagebox

class Counting(ttk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.paid = tk.StringVar()
        self.sick = tk.StringVar()
        self.clk_in = tk.StringVar()
        self.clk_out = tk.StringVar()
        self.date = tk.StringVar()
        self.double_money_day = tk.StringVar()
        self.create_widgets()
            
    def create_widgets(self):
        clk_in_label = ttk.Label(self, text="Beblokkolás")
        clk_out_label = ttk.Label(self, text="Kiblokkolás")
        self.sick_label = ttk.Label(self, text="Táppénzes nap")
        self.paid_label = ttk.Label(self, text="Szabadság")
        self.double_money_day_label = ttk.Label(self, text="Dupla béres nap?\n(Nem ünnepnap!)")
        choosen_day = ttk.Label(self, text="")
        
        
        self.double_money_day_check = ttk.Checkbutton(self,text="Dupla béres nap?\n(Nem ünnepnap!)", textvariable=self.double_money_day)
        self.sick_entry = ttk.Entry(self, width=5, textvariable=self.sick)
        self.sick_entry.insert(0, "0")
        self.paid_entry = ttk.Entry(self, width=5, textvariable=self.paid)
        self.paid_entry.insert(0, "0")
        clk_in_entry = ttk.Entry(self, width=5, textvariable=self.clk_in)
        clk_in_entry.insert(0, "6:00")
        clk_out_entry = ttk.Entry(self, width=5, textvariable=self.clk_out)
        clk_out_entry.insert(0, "14:20")
        self.calendar = Calendar(self, selectmode="day", firstweekday="monday", showweeknumbers=False, locale="hu_HU", foreground="red", selectforeground="white")
        

        self.sick_label.grid(column=0, row=0)
        self.paid_label.grid(column=1, row=0)
        self.double_money_day_label.grid(column=2, row=0)

        self.sick_entry.grid(column=0, row=1)
        self.paid_entry.grid(column=1, row=1)
        self.double_money_day_check.grid(column=2, row=1)
        
        clk_in_label.grid(column=0, row=2, padx=20)
        clk_out_label.grid(column=1, row=2, padx=20)    
        
        clk_in_entry.grid(column=0, row=3, padx=20)
        clk_out_entry.grid(column=1, row=3, padx=20)
        
        self.calendar.grid(column=0, row=4, pady=20, columnspan=3)
        choosen_day.grid(column=0, row=5, columnspan=3, pady=20)
        ttk.Button(self,text="Add", command=self.add).grid(column=1, row=6, pady=10)
        ttk.Button(self,text="Count",command=lambda: self.controller.show_frame(Counting)).grid(column=2, row=6, pady=10)
        from start_page import StartPage    
        ttk.Button(self, text="Vissza", command=lambda: self.controller.show_frame(StartPage))
        
    def add(self):
        self.date.set(self.calendar.get_date()) 
        self.calendar.config(selectforeground="green")
        self.controller.logics.paid_off = int(self.paid.get())
        self.controller.logics.sick = int(self.sick.get())
        self.controller.logics.double = self.double_money_day.get()
        print(self.controller.logics.double)
        date = self.date.get()
        
        if self.error_handling(date):
            try:
                self.controller.logics.counting_hours(self.controller.logics.convert_to_decimal(self.clk_in.get()), self.controller.logics.convert_to_decimal(self.clk_out.get()), self.double_money, date)
            except ValueError:
                messagebox.showerror("Hiba", "Hibás munkaidő intervallum!")
                
    def error_handling(self, date):
        holdiay_2023 = [
            "2023. 01. 01.",
            "2023. 03. 15.",
            "2023. 04. 07.",
            "2023. 04. 09.",
            "2023. 04. 10.",
            "2023. 05. 01.",
            "2023. 05. 29.",
            "2023. 08. 20.",
            "2023. 10. 23.",
            "2023. 11. 01.",
            "2023. 12. 26."
        ]  
        c_in = self.clk_in.get()
        c_out = self.clk_out.get()
        c_in_len = len(c_in)
        c_out_len = len(c_out)
        
        # incorrect date format
        
        if ':' not in c_in or int(c_in[0:c_in.index(':', 0, c_in_len - 1)]) > 24 or int(c_in[c_in.index(':', 0, c_in_len - 1) + 1:]) > 60:
            messagebox.showerror("Hiba", "Dátumformátum nem megfelelő!")
            return False
        
        if ':' not in c_out or int(c_out[0:c_out.index(':', 0, c_out_len - 1)]) > 24 or int(c_out[c_out.index(':', 0, c_out_len - 1) + 1:]) > 60:
            messagebox.showerror("Hiba", "Dátumformátum nem megfelelő!")
            return False
        
        # day duplication and double money by day check
        if date not in self.controller.logics.workdays:
            if date in holdiay_2023:
                self.double_money = True
            else:
                self.double_money = False
            return True
        else:
            messagebox.showerror("Hiba", "Erre a napra már megadtal blokkolást!")
            return False
                         