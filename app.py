from tkinter import *
from tkinter import messagebox
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
        self.is_student = IntVar()
        self.salary = 0
        self.logics = Logics()
        self.solutions = []
        self.double_money = False
        self.create_widgets()
    
    def create_widgets(self):
        # labels
        wage_label = Label(self, text="Wage")
        age_label = Label(self, text="Age")
        self.sick_label = Label(self, text="Sick")
        self.paid_label = Label(self, text="Holiday")
        clk_in_label = Label(self, text="Clock in")
        clk_out_label = Label(self, text="Clock out")
        
        # entries
        wage_entry = Entry(self, width=5, textvariable=self.wage)
        wage_entry.insert(0, "1565")
        age_entry = Entry(self, width=5, textvariable=self.age)
        age_entry.insert(0, "23")
        self.sick_entry = Entry(self, width=5, textvariable=self.sick)
        self.sick_entry.insert(0, "0")
        self.paid_entry = Entry(self, width=5, textvariable=self.paid)
        self.paid_entry.insert(0, "0")
        clk_in_entry = Entry(self, width=5, textvariable=self.clk_in)
        clk_in_entry.insert(0, "6:00")
        clk_out_entry = Entry(self, width=5, textvariable=self.clk_out)
        clk_out_entry.insert(0, "14:20")
        self.calendar = Calendar(self, selectmode="day", firstweekday="monday", showweeknumbers=False, locale="hu_HU", foreground="red", selectforeground="white")
        student = Checkbutton(self, text="Diák vagyok", variable=self.is_student, command=self.student_def)
        
        #put on screen
        wage_label.grid(column=0, row=0, padx=20)
        age_label.grid(column=1, row=0, padx=20)
        self.sick_label.grid(column=2, row=0, padx=20)
        self.paid_label.grid(column=3, row=0, padx=20)
             
        wage_entry.grid(column=0, row=1, padx=20)
        age_entry.grid(column=1, row=1, padx=20)

        
        clk_in_label.grid(column=0, row=2, padx=20)
        clk_out_label.grid(column=1, row=2, padx=20)    
        
        clk_in_entry.grid(column=0, row=3, padx=20)
        clk_out_entry.grid(column=1, row=3, padx=20)
        student.grid(column=2, row=3, padx=20, columnspan=2)
        
        self.calendar.grid(column=0, row=4, columnspan=4, pady=20)
    
        Button(self,text="Add", command=self.add).grid(column=1, row=5, pady=10)
        Button(self,text="Count", command=self.show_data).grid(column=2, row=5, pady=10)  

    def student_def(self):
        if not self.is_student:
            self.sick_entry.grid()
            self.paid_entry.grid()
            self.sick_label.grid()
            self.paid_label.grid()
        if self.is_student:
            self.sick_label.grid_forget()
            self.paid_label.grid_forget()
            self.sick_entry.grid_forget()
            self.paid_entry.grid_forget()
            
    def add(self):   
        self.date.set(self.calendar.get_date()) 
        self.calendar.config(selectforeground="green")
        self.logics.age = int(self.age.get())
        self.logics.paid_off = int(self.paid.get())
        self.logics.sick = int(self.sick.get())
        self.logics.wage = int(self.wage.get())
        date = self.date.get()
        
        if self.error_handling(date):
            self.logics.counting_hours(self.logics.convert_to_decimal(self.clk_in.get()), self.logics.convert_to_decimal(self.clk_out.get()), self.double_money, date)
    
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
        if date not in self.logics.workdays:
            if date in holdiay_2023:
                self.double_money = True
            else:
                self.double_money = False
            return True
        else:
            messagebox.showerror("Hiba", "Erre a napra már megadtal blokkolást!")
            return False
                         
    def show_data(self):
        self.logics.counting_money()
        top = Toplevel()
        top.title("Calculations")
        top.geometry("600x400")
        row_index = 0
        Label(top, text=f"Date").grid(row=0, column=0, sticky='W', padx=30)
        Label(top, text=f"Base").grid(row=0, column=1, sticky='W', padx=15)
        Label(top, text=f"30%").grid(row=0, column=2, sticky='W', padx=15)
        Label(top, text=f"40%").grid(row=0, column=3, sticky='W', padx=15)
        Label(top, text=f"100%").grid(row=0, column=4, sticky='W', padx=15)
        
        for row_index,data in enumerate(self.logics.datas):
            Label(top, text=f"{data.day}").grid(row=row_index + 1, column=0, sticky='W', padx=30)
            Label(top, text=f"{data.base_hours:.2f}").grid(row=row_index + 1, column=1, sticky='W', padx=15)
            Label(top, text=f"{data.thirty_percent:.2f}").grid(row=row_index + 1, column=2, sticky='W', padx=15)
            Label(top, text=f"{data.fourty_percent:.2f}").grid(row=row_index + 1, column=3, sticky='W', padx=15)
            Label(top, text=f"{data.hundred_percent:.2f}").grid(row=row_index + 1, column=4, sticky='W', padx=15)
            
        Label(top, text=f"Total").grid(row=row_index + 2, column=0, sticky='W', padx=30)
        Label(top, text=f"{self.logics.total_base:.2f}").grid(row=row_index + 2, column=1, sticky='W', padx=15)
        Label(top, text=f"{self.logics.total_thirty:.2f}").grid(row=row_index + 2, column=2, sticky='W', padx=15)
        Label(top, text=f"{self.logics.total_fourty:.2f}").grid(row=row_index + 2, column=3, sticky='W', padx=15)
        Label(top, text=f"{self.logics.total_hundred:.2f}").grid(row=row_index + 2, column=4, sticky='W', padx=15)
        
        Label(top, text=f"Money").grid(row=row_index + 3, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(self.logics.total_base) * self.logics.wage}").grid(row=row_index + 3, column=1, sticky='W', padx=15)
        Label(top, text=f"{round(self.logics.total_thirty) * self.logics.wage}").grid(row=row_index + 3, column=2, sticky='W', padx=15)
        Label(top, text=f"{round(self.logics.total_fourty) * self.logics.wage}").grid(row=row_index + 3, column=3, sticky='W', padx=15)
        Label(top, text=f"{round(self.logics.total_hundred) * self.logics.wage}").grid(row=row_index + 3, column=4, sticky='W', padx=15)
        
        Label(top, text=f"Brutto salary").grid(row=row_index + 4, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(self.logics.brutto_money)}").grid(row=row_index + 4, column=1, sticky='W', padx=15)
        
        Label(top, text=f"Nett salary").grid(row=row_index + 5, column=0, sticky='W', padx=30)
        Label(top, text=f"{round(self.logics.nett_money)}").grid(row=row_index + 5, column=1, sticky='W', padx=15)
    
def main():
    app = SalaryCounter()
    app.mainloop()
    
if __name__ == "__main__":
    main()
