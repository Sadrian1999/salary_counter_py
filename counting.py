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
        #TODO
        pass