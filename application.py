import tkinter as tk
from tkinter import ttk
from start_page import StartPage
from counting import Counting
from calculations import Calculations
from settings import Settings
  
class SalaryCounter(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.settings()
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

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        
    def settings(self):
        self.title("Salary Counter")
        self.geometry("400x400")
        self.resizable(0,0)
        
def main():
    app = SalaryCounter()
    app.mainloop()
    
if __name__ == "__main__":
    main()