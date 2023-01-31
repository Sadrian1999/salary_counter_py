from tkinter import ttk
import tkinter as tk
from counting import Counting
from previous import Previous
from settings import Settings


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()
        
    def create_widgets(self):
        new_calculation_label = ttk.Label(self, text="Új bérszámolás")
        previous_calculations_label = ttk.Label(self, text="Előző számítások")
        settings_label = ttk.Label(self, text="Beállítások")
        exit_label = ttk.Label(self, text="Kilépés")
        
        new_calculation_label.grid(column=0, row=1, pady=2, padx=10)
        previous_calculations_label.grid(column=0, row=2, pady=2, padx=10)
        settings_label.grid(column=0, row=3, pady=2, padx=10)
        exit_label.grid(column=0, row=4, pady=2, padx=10)
        
        new_calculation_label.bind("<Button-1>", lambda x: self.controller.show_frame(Counting))
        previous_calculations_label.bind("<Button-1>", lambda x: self.controller.show_frame(Previous))
        settings_label.bind("<Button-1>", lambda x: self.controller.show_frame(Settings))
        exit_label.bind("<Button-1>", lambda x: exit())
