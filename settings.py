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
        
        self.wage = StringVar()
        self.age = StringVar()
        self.position = StringVar()
        self.aplication_type = StringVar()
        self.job_time = StringVar()
        self.tax_free = BooleanVar()
        
        settings = ttk.Label(self, text="Beállítások")
        wage_label = ttk.Label(self, text="Órabér")
        age_label = ttk.Label(self, text="Életkor")
        position_label = ttk.Label(self, text="Pozíció")
        aplication_type_label = ttk.Label(self, text="Alkalmazás típusa")
        job_time_label = ttk.Label(self, text="Munkaidő")
        tax_free_label = ttk.Label(self, text="Adóköteles")
        
        wage_entry = ttk.Entry(self, textvariable=self.wage, width=4)
        age_entry = ttk.Entry(self, textvariable=self.age, width=4)
        position_menu = ttk.OptionMenu(self, self.position, pos_options[0], *pos_options)
        aplication_type_menu = ttk.OptionMenu(self, self.aplication_type, app_options[0], *app_options)
        job_time_menu = ttk.OptionMenu(self, self.job_time, time_options[0], *time_options)
        tax_free_check = ttk.Checkbutton(self, variable=self.tax_free)
        
        settings.grid(column=0, row=0, columnspan=2, padx=10)
        wage_label.grid(column=0, row=1, sticky=W, padx=10)
        age_label.grid(column=0, row=2, sticky=W, padx=10)
        position_label.grid(column=0, row=3, sticky=W, padx=10)
        aplication_type_label.grid(column=0, row=4, sticky=W, padx=10)
        job_time_label.grid(column=0, row=5, sticky=W, padx=10)
        tax_free_label.grid(column=0, row=6, sticky=W, padx=10)
        
        wage_entry.grid(column=1, row=1, sticky=W)
        age_entry.grid(column=1, row=2, sticky=W)
        position_menu.grid(column=1, row=3, sticky=W)
        aplication_type_menu.grid(column=1, row=4, sticky=W)
        job_time_menu.grid(column=1, row=5, sticky=W)
        tax_free_check.grid(column=1, row=6, sticky=W)
        
        save = Button(self, text="Mentés", command=self.write_data)
        save.grid(column=0, row=7)
        from start_page import StartPage
        back = Button(self, text="Vissza", command=lambda: self.controller.show_frame(StartPage))
        back.grid(column=1, row=7)

    def write_data(self):
        w = self.wage.get()
        ag = self.age.get()
        p = self.position.get()
        ap = self.aplication_type.get()
        t = self.tax_free.get()
        j = self.job_time.get()
        
        if ap == "Diák":
            j = '-'
        try:
            int(w)
        except Exception:
            return messagebox.showerror("Hiba", "Hibás órabér")
        
        try:
            int(ag)
        except Exception:
            return messagebox.showerror("Hiba", "Hibás életkor")
        
        if int(w) > 10000 or int(w) < 1000:
            return messagebox.showerror("Hiba", "Hibás órabér")
        
        if int(ag) > 99 or int(ag) < 15:
            return messagebox.showerror("Hiba", "Hibás életkor")
        
        with open("user_data.txt", "wt") as file:
            for element in (w, ag, p, ap, j, t):
                file.write(str(element) + "\n")
        return messagebox.showinfo("Siker", "Adatok sikeresen mentve")

        