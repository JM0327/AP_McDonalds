import tkinter as tk
from tkinter import messagebox
import pandas as pd
from interface2 import AMRPage
import ttkbootstrap as ttk
from saveinfo import AllInfo

class InfoPage:

    def __init__(self, master):

        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('650x650')  # size

        # Drop Down box

        clickgender = ["Drop down choose",
                       "female",
                       "male"]
        clicksport = ["Drop down choose",
                      "Sedentary",
                      "Lightly active",
                      "Moderately active",
                      "Active"]

        self.inputgender = tk.StringVar()
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()

        self.page = tk.Frame(window)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='Gender(male/female): ', anchor="ne", width=15).grid(row=1, column=0,pady=20)
        ttk.OptionMenu(self.page, self.inputgender, *clickgender, style="dark").grid(row=1, column=3)

        tk.Label(self.page, text='Weight(unit:kg): ', anchor="ne",  width=15).grid(row=2, column=0,pady=20)
        tk.Spinbox(self.page, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=15).grid(row=2, column=3)

        tk.Label(self.page, text='Height(unit:cm): ', anchor="ne",  width=15).grid(row=3, column=0,pady=20)
        tk.Spinbox(self.page, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=15).grid(row=3, column=3)

        tk.Label(self.page, text='Age(integer): ', anchor="ne", width=15).grid(row=4, column=0,pady=20)
        tk.Spinbox(self.page, from_=10, to=100, textvariable=self.inputage, wrap=False, width=15).grid(row=4, column=3)

        tk.Label(self.page, text='Sport frequency: ', anchor="ne", width=15).grid(row=5, column=0, pady=20)
        ttk.OptionMenu(self.page, self.inputsport, *clicksport, style="dark").grid(row=5, column=3)

        ttk.Button(self.page, text='Calculate', command=lambda: [self.bmramr(), self.popup()], width=10,style='success.TButton')\
            .grid(row=6, column=0,pady=20)
        ttk.Button(self.page, text='Next', command=lambda:[self.check()], width=10, style='success.TButton').grid(row=6, column=3)
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=10, style='success.TButton').grid(row=6, column=5)

        # Creat a notebook frame to put the amr result in
        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(pady=10, expand=True)
        self.frame = ttk.Frame(self.notebook, width=600, height=100, style="dark")
        self.frame.pack(fill='both', expand=True)
        self.frame.pack_propagate(0)
        self.notebook.add(self.frame, text='Your AMR')


    def bmramr(self):
        global bmr, amr, breakfastamr, lunchamr, dinneramr

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "male":
            bmr = 13.75 * int(weight) + 5.003 * int(height) - 6.755* int(age) + 66.47
        else:
            bmr = 9.563 * int(weight) + 1.850 * int(height) - 4.676 * int(age) + 655.1

        if sport == "Sedentary":
            amr = round(bmr * 1.2, 2)
        elif sport == "Lightly active":
            amr = round(bmr * 1.375, 2)
        elif sport == "Moderately active":
            amr = round(bmr * 1.55, 2)
        elif sport == "Active":
            amr = round(bmr * 1.725, 2)
        else:
            amr = round(bmr * 1.9, 2)

        if amr > 0:
            breakfastamr = int(amr * 0.35)
            lunchamr = int(amr * 0.35)
            dinneramr = int(amr * 0.30)

    def popup(self):
        response = messagebox.askquestion("Q", "Do you want to know your AMR")
        if response == "yes":
            ttk.Label(self.frame, text=f"Your AMR is {amr} calories per day.", anchor='sw',font=(30),style="light").pack()
            ttk.Label(self.frame, text=f"AMR for breakfast is {breakfastamr} calories.", anchor='sw',font=(30),style="light").pack()
            ttk.Label(self.frame, text=f"AMR for lunch is {lunchamr} calories.", anchor='sw',font=(30),style="light").pack()
            ttk.Label(self.frame, text=f"AMR for dinner is {dinneramr} calories.", anchor='sw',font=(30),style="light").pack()
        else:
            ttk.Label(self.frame, text="oops!",style="dark").pack()


    def check(self):

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "female" or gender == "male" or not weight is None or not height is None or not sport is None or not age is None:
            self.page.destroy()
            AMRPage(self.page)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')



if __name__ == '__main__':
    window = tk.Tk()
    InfoPage(master=window)
    window.mainloop()

