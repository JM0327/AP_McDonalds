import tkinter as tk
from tkinter import messagebox
import pandas as pd
from interface2 import Recommendation
import ttkbootstrap as ttk
from saveinfo import AllInfo

class InfoPage:

    def __init__(self, master):
        # here is creating the general window for interface
        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('650x650')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

        # Drop Down box content
        clickgender = ["Drop down",
                       "female",
                       "male"]
        clicksport = ["Drop down",
                      "Sedentary",
                      "Lightly active",
                      "Moderately active",
                      "Active",
                      "Very active"]

        # here is getting the info users put in
        self.inputgender = tk.StringVar()
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()

        # here is creating a series of buttom and box that input the inforamtion
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='Gender(male/female): ', anchor="nw", width=15).grid(row=1, column=0,pady=20)
        ttk.OptionMenu(self.page, self.inputgender, *clickgender, style="dark").grid(row=1, column=2)

        tk.Label(self.page, text='Weight(unit:kg): ', anchor="nw",  width=15).grid(row=2, column=0,pady=20)
        tk.Spinbox(self.page, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=10).grid(row=2, column=2)

        tk.Label(self.page, text='Height(unit:cm): ', anchor="nw",  width=15).grid(row=3, column=0,pady=20)
        tk.Spinbox(self.page, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=10).grid(row=3, column=2)

        tk.Label(self.page, text='Age(integer): ', anchor="nw", width=15).grid(row=4, column=0,pady=20)
        tk.Spinbox(self.page, from_=10, to=100, textvariable=self.inputage, wrap=False, width=10).grid(row=4, column=2)

        tk.Label(self.page, text='Sport frequency: ', anchor="nw", width=15).grid(row=5, column=0, pady=20)
        ttk.OptionMenu(self.page, self.inputsport, *clicksport, style="dark").grid(row=5, column=2)

        tk.Label(self.page, text='        ').grid(row=6, column=1, pady=20) #dummy column
        tk.Label(self.page, text='           ').grid(row=6, column=3, pady=20)  # dummy column

        ttk.Button(self.page, text='Explanation', command=lambda: [self.sportexplanation()], width=10,
                   style='info-link').grid(row=5, column=4)

        ttk.Button(self.page, text='Calculate', command=lambda: [self.bmramr(), self.amrpopup()], width=10,style='success.TButton')\
            .grid(row=6, column=0,pady=20, sticky='w')
        ttk.Button(self.page, text='Next', command=lambda:[self.check()], width=10, style='success.TButton').grid(row=6, column=2)
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=10, style='success.TButton').grid(row=6, column=4)

        # Creat a notebook frame to put the amr result in
        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(pady=10, expand=True)
        self.frame1 = ttk.Frame(self.notebook, width=600, height=120, style="dark")
        self.frame2 = ttk.Frame(self.notebook, width=600, height=120, style="dark")
        self.frame1.pack(fill='both', expand=True)
        self.frame1.pack_propagate(0)
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack_propagate(0)
        self.notebook.add(self.frame1, text='Your AMR')
        self.notebook.add(self.frame2, text='AMR explanation')

        # amr explanation
        ttk.Label(self.frame2, text="AMR represents the amount of calories you need to intake each day to stay "
                                    "at your current weight.", anchor='sw', font=(30), style="info").pack(pady=5)
        ttk.Label(self.frame2, text="AMR for breakfast and lunch are 35% of AMR per day, respectively.", anchor='sw',
                  font=(30), style="info", width=200).pack(pady=5)
        ttk.Label(self.frame2, text="AMR for dinner is 30% of AMR per day.", anchor='sw', font=(30), style="info",
                  width=200).pack(pady=5)


    # giving information of explaining sport frequency drop down choice
    def sportexplanation(self):
        top = tk.Toplevel()
        top.title("Sport frequency explanation")
        ttk.Label(top, text="Sedentary: little or no exercise", anchor='sw', font=(30), style="info").pack(pady=5)
        ttk.Label(top, text="Lightly active: exercise 1–3 days/week)", anchor='sw', font=(30), style="info").pack(pady=5)
        ttk.Label(top, text="Moderately active: exercise 3–5 days/week)", anchor='sw', font=(30), style="info").pack(pady=5)
        ttk.Label(top, text="Active: exercise 6–7 days/week)", anchor='sw', font=(30), style="info").pack(pady=5)
        ttk.Label(top, text="Very active: hard exercise 6–7 days/week)", anchor='sw', font=(30), style="info").pack(pady=5)

    # function for calculating the amr
    def bmramr(self):
        global bmr, amr, breakfastamr, lunchamr, dinneramr, gender, weight, height, age, sport

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "female" or gender == "male" and not weight is None and not height is None and not age is None and sport == "Sedentary" or sport=="Lightly active" or sport=="Moderately active" or sport=="Active":
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
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')

        if amr > 0:
            breakfastamr = int(amr * 0.35)
            lunchamr = int(amr * 0.35)
            dinneramr = int(amr * 0.30)
        else:
            breakfastamr = "?"
            lunchamr = "?"
            dinneramr= "?"

    # create a popup window that can initiate the display of calculation results
    def amrpopup(self):
        if gender == "female" or gender == "male" and not weight is None and not height is None and not age is None and sport == "Sedentary" or sport=="Lightly active" or sport=="Moderately active" or sport=="Active":
            response = messagebox.askquestion("Q", "Do you want to know your AMR?")
            if response == "yes":
                ttk.Label(self.frame1, text=f"Your AMR is {amr} calories per day.", anchor='sw', font=(30), style="info").pack(pady=5)
                ttk.Label(self.frame1, text=f"AMR for breakfast is {breakfastamr} calories.", anchor='sw', font=(30),style="info").pack(pady=5)
                ttk.Label(self.frame1, text=f"AMR for lunch is {lunchamr} calories.", anchor='sw', font=(30), style="info").pack(pady=5)
                ttk.Label(self.frame1, text=f"AMR for dinner is {dinneramr} calories.", anchor='sw', font=(30), style="info").pack(pady=5)

            else:
                ttk.Label(self.frame1, text="oops!",style="dark").pack()
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')

    def cleanamr(self):
        pass

    # check if all the information already input and turn to the next page.
    def check(self):

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "female" or gender == "male" or not weight is None or not height is None or not sport is None or not age is None:
            self.page.destroy()
            self.notebook.destroy()
            Recommendation(self.window)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')



if __name__ == '__main__':
    window = tk.Tk()
    InfoPage(master=window)
    window.mainloop()

