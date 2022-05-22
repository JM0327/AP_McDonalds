from Interface_2 import *
from tkinter import messagebox
import ttkbootstrap as ttk


class InfoPage:

    def __init__(self, master):
        # here is creating the general window for interface
        style = ttk.Style(theme='flatly')

        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

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

        ttk.Label(self.page, text='Gender(male/female): ', anchor="nw", width=15, style='info').grid(row=1, column=0,
                                                                                                     pady=25)
        ttk.OptionMenu(self.page, self.inputgender, *clickgender, style="info-outline").grid(row=1, column=2)

        ttk.Label(self.page, text='Weight(unit:kg): ', anchor="nw", width=15, style='info').grid(row=2, column=0,
                                                                                                 pady=25)
        tk.Spinbox(self.page, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=10).grid(row=2,
                                                                                                          column=2)

        ttk.Label(self.page, text='Height(unit:cm): ', anchor="nw", width=15, style='info').grid(row=3, column=0,
                                                                                                 pady=25)
        tk.Spinbox(self.page, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=10).grid(row=3,
                                                                                                           column=2)

        ttk.Label(self.page, text='Age(integer): ', anchor="nw", width=15, style='info').grid(row=4, column=0, pady=25)
        tk.Spinbox(self.page, from_=10, to=100, textvariable=self.inputage, wrap=False, width=10).grid(row=4, column=2)

        ttk.Label(self.page, text='Sport frequency: ', anchor="nw", width=15, style='info').grid(row=5, column=0,
                                                                                                 pady=25)
        ttk.OptionMenu(self.page, self.inputsport, *clicksport, style="info-outline").grid(row=5, column=2)

        tk.Label(self.page, text='     ').grid(row=6, column=1, pady=5)  # dummy column
        tk.Label(self.page, text=' ').grid(row=6, column=6, pady=5)  # dummy column

        ttk.Button(self.page, text='Next', command=lambda: [self.gointerface2()], width=5,
                   style='success.TButton').grid(row=7, column=4)
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').grid(row=7,
                                                                                                          column=7)

    def gointerface2(self):

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "female" or gender == "male" and not sport is None:
            self.page.destroy()
            AMRPage(self.window, gender=gender, height=height, weight=weight, age=age, sport=sport)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')

