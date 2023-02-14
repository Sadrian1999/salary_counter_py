import tkinter as tk
from tkinter import ttk

class Calculations(ttk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.controller.logics.counting_money()
		self.create_widgets()
			
	def create_widgets(self):
		tk.Label(self, text=f"Date").grid(row=0, column=0, sticky='W', padx=30)
		tk.Label(self, text=f"Base").grid(row=0, column=1, sticky='W', padx=15)
		tk.Label(self, text=f"30%").grid(row=0, column=2, sticky='W', padx=15)
		tk.Label(self, text=f"40%").grid(row=0, column=3, sticky='W', padx=15)
		tk.Label(self, text=f"100%").grid(row=0, column=4, sticky='W', padx=15)

		for row_index,data in enumerate(self.controller.logics.datas):
			tk.Label(self, text=f"{data.day}").grid(row=row_index + 1, column=0, sticky='W', padx=30)
			tk.Label(self, text=f"{data.base_hours:.2f}").grid(row=row_index + 1, column=1, sticky='W', padx=15)
			tk.Label(self, text=f"{data.thirty_percent:.2f}").grid(row=row_index + 1, column=2, sticky='W', padx=15)
			tk.Label(self, text=f"{data.fourty_percent:.2f}").grid(row=row_index + 1, column=3, sticky='W', padx=15)
			tk.Label(self, text=f"{data.hundred_percent:.2f}").grid(row=row_index + 1, column=4, sticky='W', padx=15)
			
		tk.Label(self, text=f"Total").grid(row=row_index + 2, column=0, sticky='W', padx=30)
		tk.Label(self, text=f"{self.controller.logics.total_base:.2f}").grid(row=row_index + 2, column=1, sticky='W', padx=15)
		tk.Label(self, text=f"{self.controller.logics.total_thirty:.2f}").grid(row=row_index + 2, column=2, sticky='W', padx=15)
		tk.Label(self, text=f"{self.controller.logics.total_fourty:.2f}").grid(row=row_index + 2, column=3, sticky='W', padx=15)
		tk.Label(self, text=f"{self.controller.logics.total_hundred:.2f}").grid(row=row_index + 2, column=4, sticky='W', padx=15)

		tk.Label(self, text=f"Money").grid(row=row_index + 3, column=0, sticky='W', padx=30)
		tk.Label(self, text=f"{round(self.controller.logics.total_base * self.controller.logics.wage) }").grid(row=row_index + 3, column=1, sticky='W', padx=15)
		tk.Label(self, text=f"{round(self.controller.logics.total_thirty * self.controller.logics.wage * 0.3)}").grid(row=row_index + 3, column=2, sticky='W', padx=15)
		tk.Label(self, text=f"{round(self.controller.logics.total_fourty * self.controller.logics.wage * 0.4)}").grid(row=row_index + 3, column=3, sticky='W', padx=15)
		tk.Label(self, text=f"{round(self.controller.logics.total_hundred * self.controller.logics.wage * 2)}").grid(row=row_index + 3, column=4, sticky='W', padx=15)

		tk.Label(self, text=f"Brutto salary").grid(row=row_index + 4, column=0, sticky='W', padx=30)
		tk.Label(self, text=f"{round(self.controller.logics.brutto_money)}").grid(row=row_index + 4, column=1, sticky='W', padx=15)

		tk.Label(self, text=f"Nett salary").grid(row=row_index + 5, column=0, sticky='W', padx=30)
		tk.Label(self, text=f"{round(self.controller.logics.nett_money)}").grid(row=row_index + 5, column=1, sticky='W', padx=15)
		
