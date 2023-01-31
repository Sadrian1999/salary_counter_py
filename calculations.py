import tkinter as tk
from tkinter import ttk

class Calculations(ttk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.create_widgets()
			
	def create_widgets(self):
		pass