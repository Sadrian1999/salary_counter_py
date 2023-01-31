from tkinter import *
from tkinter import ttk, messagebox

class Settings(ttk.Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
            
    def create_widgets(self):
        pos_options = (
            "Éttermi dolgozó", 
            "Tréner", 
            "Koordinátor", 
            "VÉM", 
            "Műszakvezető",
            "II. Helyettes",
            "I. Helyettes",
            "Étteremvezető"
        )
        
        time_options = (
            "8 órás",
            "6 órás",
            "4 órás"
        )
        
        app_options = (
            "Állandós",
            "Diák"
        )
        
        wage = StringVar()
        age = StringVar()
        position = StringVar()
        aplication_type = StringVar()
        job_time = StringVar()
        tax_free = BooleanVar()
        
        settings = ttk.Label(self, text="Beállítások")
        wage_label = ttk.Label(self, text="Órabér")
        age_label = ttk.Label(self, text="Életkor")
        position_label = ttk.Label(self, text="Pozíció")
        aplication_type_label = ttk.Label(self, text="Alkalmazás típusa")
        job_time_label = ttk.Label(self, text="Munkaidő")
        tax_free_label = ttk.Label(self, text="Adóköteles")
        
        wage_entry = ttk.Entry(self, textvariable=wage)
        age_entry = ttk.Entry(self, textvariable=age)
        position_menu = ttk.OptionMenu(self, position, pos_options[0], *pos_options)
        aplication_type_menu = ttk.OptionMenu(self, aplication_type, app_options[0], *app_options)
        job_time_menu = ttk.OptionMenu(self, job_time, time_options[0], *time_options)
        tax_free_check = ttk.Checkbutton(self, variable=tax_free)
        
        settings.grid(column=0, row=0, columnspan=2)
        wage_label.grid(column=0, row=1)
        age_label.grid(column=0, row=2)
        position_label.grid(column=0, row=3)
        aplication_type_label.grid(column=0, row=4)
        job_time_label.grid(column=0, row=5)
        tax_free_label.grid(column=0, row=6)
        
        wage_entry.grid(column=1, row=1)
        age_entry.grid(column=1, row=2)
        position_menu.grid(column=1, row=3)
        aplication_type_menu.grid(column=1, row=4)
        job_time_menu.grid(column=1, row=5)
        tax_free_check.grid(column=1, row=6)
        
        b = Button(self, text="asdasdsa", command=lambda x: print(wage, age, position, aplication_type, job_time, tax_free, sep="\n"))
        b.grid(column=0, row=7,columnspan=2)