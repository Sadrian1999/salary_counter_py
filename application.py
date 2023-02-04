import tkinter as tk
from tkinter import ttk
from start_page import StartPage
from counting import Counting
from calculations import Calculations
from settings import Settings
from logics import Logics
  
class SalaryCounter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.logics = Logics()
        self.settings()
        self.read_data()

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def settings(self):
        self.title("Salary Counter")
        self.geometry("400x400")
        self.resizable(0,0)
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        self.frames = {} 
        for F in (StartPage, Counting, Calculations, Settings):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew")
            
        self.show_frame(StartPage)
        
    def read_data(self):
        with open("user_data.txt", "rt") as file:
            lines = file.readlines()
        self.logics.wage = int(lines[0].rstrip("\n"))
        self.logics.age = int(lines[1].rstrip("\n"))
        self.logics.is_vem = True if lines[2].rstrip("\n") == "VÉM" else False
        
        print(self.logics.is_vem)
def main():
    app = SalaryCounter()
    app.mainloop()
    
if __name__ == "__main__":
    main()