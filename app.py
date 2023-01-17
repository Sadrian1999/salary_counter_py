from tkinter import *
from tkcalendar import Calendar
from logics import Logics

class SalaryCounter(Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Salary Counter")
        self.geometry("400x400")
        self.resizable(0,0)
        self.wage = StringVar()
        self.age = StringVar()
        self.paid = StringVar()
        self.sick = StringVar()
        self.clk_in = StringVar()
        self.clk_out = StringVar()
        self.date = StringVar()
        self.salary = 0
        self.logics = Logics()
        self.solutions = []
        self.create_widgets()
    
    def create_widgets(self):
        # labels
        wage_label = Label(self, text="Wage")
        age_label = Label(self, text="Age")
        sick_label = Label(self, text="Sick")
        paid_label = Label(self, text="Holiday")
        clk_in_label = Label(self, text="Clock in")
        clk_out_label = Label(self, text="Clock out")
        
        # entries
        wage_entry = Entry(self, width=5, textvariable=self.wage)
        wage_entry.insert(0, "1565")
        age_entry = Entry(self, width=5, textvariable=self.age)
        age_entry.insert(0, "23")
        sick_entry = Entry(self, width=5, textvariable=self.sick)
        sick_entry.insert(0, "0")
        paid_entry = Entry(self, width=5, textvariable=self.paid)
        paid_entry.insert(0, "0")
        clk_in_entry = Entry(self, width=5, textvariable=self.clk_in)
        clk_in_entry.insert(0, "6:00")
        clk_out_entry = Entry(self, width=5, textvariable=self.clk_out)
        clk_out_entry.insert(0, "14:20")
        self.calendar = Calendar(self, selectmode="day", firstweekday="monday", showweeknumbers=False, locale="hu_HU", foreground="red", selectforeground="white")
        
        #put on screen
        wage_label.grid(column=0, row=0, padx=20)
        age_label.grid(column=1, row=0, padx=20)
        sick_label.grid(column=2, row=0, padx=20)
        paid_label.grid(column=3, row=0, padx=20)
             
        wage_entry.grid(column=0, row=1, padx=20)
        age_entry.grid(column=1, row=1, padx=20)
        sick_entry.grid(column=2, row=1, padx=20)
        paid_entry.grid(column=3, row=1, padx=20)
        
        clk_in_label.grid(column=0, row=2, padx=20)
        clk_out_label.grid(column=1, row=2, padx=20)     
        
        clk_in_entry.grid(column=0, row=3, padx=20)
        clk_out_entry.grid(column=1, row=3, padx=20)
        
        self.calendar.grid(column=0, row=4, columnspan=4, pady=20)
    
        Button(self,text="Add", command=self.add).grid(column=1, row=5, pady=10)
        Button(self,text="Count", command=self.show_data).grid(column=2, row=5, pady=10)  

    def add(self):
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
        
        self.date.set(self.calendar.get_date()) 
        if self.date.get() in holdiay_2023:
            double_money = True
        else:
            double_money = False
        if self.date.get() in self.logics.date:
            Label(self, text="A megadott dátum már szerepel a")
        else:
            print("apad")
            self.logics.date.append(self.date.get())
        self.calendar.config(selectforeground="green")
        self.logics.age = int(self.age.get())
        self.logics.paid_off = int(self.paid.get())
        self.logics.sick = int(self.sick.get())
        self.logics.wage = int(self.wage.get())
        self.solutions.append([self.logics.date, self.logics.base_hours, self.logics.thirty_percent, self.logics.fourty_percent, self.logics.hundred_percent])
        self.logics.counting_hours(self.logics.convert_to_decimal(self.clk_in.get()), self.logics.convert_to_decimal(self.clk_out.get()), double_money)
        self.salary += self.logics.counting_money()
    
    def show_data(self):
        top = Toplevel()
        top.title("Calculations")
        top.geometry("600x400")
        
        Label(top, text=f"Date").grid(row=0, column=0, sticky='W', padx=30)
        Label(top, text=f"Base").grid(row=0, column=1, sticky='W', padx=15)
        Label(top, text=f"30%").grid(row=0, column=2, sticky='W', padx=15)
        Label(top, text=f"40%").grid(row=0, column=3, sticky='W', padx=15)
        Label(top, text=f"100%").grid(row=0, column=4, sticky='W', padx=15)
        
        for index, solution in enumerate(self.solutions):
            print(solution)
            Label(top, text=f"{solution[0][index]}").grid(row=index + 1, column=0, sticky='W', padx=30)
            Label(top, text=f"{solution[1][index]:.2f}").grid(row=index + 1, column=1, sticky='W', padx=15)
            Label(top, text=f"{solution[2][index]:.2f}").grid(row=index + 1, column=2, sticky='W', padx=15)
            Label(top, text=f"{solution[3][index]:.2f}").grid(row=index + 1, column=3, sticky='W', padx=15)
            Label(top, text=f"{solution[4][index]:.2f}").grid(row=index + 1, column=4, sticky='W', padx=15)
            
        Label(top, text=f"Total").grid(row=index + 2, column=0, sticky='W', padx=30)
        Label(top, text=f"{sum(self.logics.base_hours):.2f}").grid(row=index + 2, column=1, sticky='W', padx=15)
        Label(top, text=f"{sum(self.logics.thirty_percent):.2f}").grid(row=index + 2, column=2, sticky='W', padx=15)
        Label(top, text=f"{sum(self.logics.fourty_percent):.2f}").grid(row=index + 2, column=3, sticky='W', padx=15)
        Label(top, text=f"{sum(self.logics.hundred_percent):.2f}").grid(row=index + 2, column=4, sticky='W', padx=15)
        
        Label(top, text=f"Money").grid(row=index + 3, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(sum(self.logics.base_hours) * self.logics.wage)}").grid(row=index + 3, column=1, sticky='W', padx=15)
        Label(top, text=f"{round(sum(self.logics.thirty_percent) * self.logics.wage)}").grid(row=index + 3, column=2, sticky='W', padx=15)
        Label(top, text=f"{round(sum(self.logics.fourty_percent) * self.logics.wage)}").grid(row=index + 3, column=3, sticky='W', padx=15)
        Label(top, text=f"{round(sum(self.logics.hundred_percent) * self.logics.wage)}").grid(row=index + 3, column=4, sticky='W', padx=15)
        
        Label(top, text=f"Brutto salary").grid(row=index + 4, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(self.logics.brutto_money)}").grid(row=index + 4, column=1, sticky='W', padx=15)
        
        Label(top, text=f"Nett salary").grid(row=index + 5, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(self.logics.brutto_money)}").grid(row=index + 5, column=1, sticky='W', padx=15)
    
def main():
    app = SalaryCounter()
    app.mainloop()
    
if __name__ == "__main__":
    main()
