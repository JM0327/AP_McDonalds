import tkinter as tk
import ttkbootstrap as ttk
from basic_information import basicinfo
from amrcalculation import *


class Page_one:

    def __init__(self, master):
        """
        create window
        """
        style = ttk.Style(theme='darkly')
        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()
        """
        Basic information
        """
        self.genderclick = basicinfo.clickgender  # information choice
        self.sportclick = basicinfo.clicksport  # information choice
        self.inputgender = tk.StringVar()
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()
        """
        page one layout set up
        """
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='Gender(male/female): ', anchor="nw", width=15).grid(row=1, column=0, pady=25)
        ttk.OptionMenu(self.page, self.inputgender, *self.genderclick, style="dark").grid(row=1, column=2)

        tk.Label(self.page, text='Weight(unit:kg): ', anchor="nw", width=15).grid(row=2, column=0, pady=25)
        tk.Spinbox(self.page, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=10).grid(row=2,
                                                                                                          column=2)

        tk.Label(self.page, text='Height(unit:cm): ', anchor="nw", width=15).grid(row=3, column=0, pady=25)
        tk.Spinbox(self.page, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=10).grid(row=3,
                                                                                                           column=2)

        tk.Label(self.page, text='Age(integer): ', anchor="nw", width=15).grid(row=4, column=0, pady=25)
        tk.Spinbox(self.page, from_=10, to=100, textvariable=self.inputage, wrap=False, width=10).grid(row=4, column=2)

        tk.Label(self.page, text='Sport frequency: ', anchor="nw", width=15).grid(row=5, column=0, pady=25)
        ttk.OptionMenu(self.page, self.inputsport, *self.sportclick, style="dark").grid(row=5, column=2)

        tk.Label(self.page, text='     ').grid(row=6, column=1, pady=5)  # dummy column
        tk.Label(self.page, text=' ').grid(row=6, column=6, pady=5)  # dummy column

        ttk.Button(self.page, text='Next', command=lambda: [self.GoPage_two()], width=5,
                   style='success.TButton').grid(row=7, column=4)
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').grid(row=7,
                                                                                                          column=7)

    def GoPage_two(self):
        self.page.destroy()
        Page_two(self.window)


class AMRResult:

    def __init__(self):
        style = ttk.Style(theme='darkly')
        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()

        user = Page_one(self)
        self.gender = user.inputgender.get()
        self.weight = user.inputweight.get()
        self.height = user.inputheight.get()
        self.age = user.inputage.get()
        self.sport = user.inputsport.get()

        self.amr, self.breakfastamr, self.lunchamr, self.dinneramr = calculation(gender=self.gender, weight=self.weight,
                                                             height=self.height,
                                                             age=self.age, sport=self.sport)
        self.window.withdraw()


class Page_two:

    def __init__(self, master):
        """
        create window
        """
        style = ttk.Style(theme='darkly')
        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()
        """
        Basic information
        """
        user = Page_one(self)
        self.gender = user.inputgender.get()
        self.weight = user.inputweight.get()
        self.height = user.inputheight.get()
        self.age = user.inputage.get()
        self.sport = user.inputsport.get()
        """
        page two layout set up
        """
        self.notebook1 = ttk.Notebook(self.window)  # create notebook 1 for amr result
        self.notebook1.pack(pady=10, expand=True)
        self.frame1 = ttk.Frame(self.notebook1, width=480, height=120, style="dark")
        self.frame1.pack(fill='both', expand=True)
        self.frame1.pack_propagate(0)
        self.notebook1.add(self.frame1, text='Your AMR')

        self.notebook2 = ttk.Notebook(self.window)  # second one for amr explanation
        self.notebook2.pack(pady=10, expand=True)
        self.frame2 = ttk.Frame(self.notebook2, width=480, height=120, style="dark")
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack_propagate(0)
        self.notebook2.add(self.frame2, text='Your AMR')

        tk.Label(self.page, text='               ').pack(side='right')  # dummy column
        tk.Label(self.page, text='               ').pack(side='right')  # dummy column
        tk.Label(self.page, text='               ').pack(side='right')  # dummy column
        ttk.Button(self.page, text='Next', command=self.GoPage_three, width=5,
                   style='success.TButton').pack(side='bottom')
        tk.Label(self.page, text='               ').pack(side='right')  # dummy column
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').pack(side='right')

    # global amr, breakfastamr, lunchamr, dinneramr
    # def calculation(self):
    #     global amr, breakfastamr, lunchamr, dinneramr
    #     amr, breakfastamr, lunchamr, dinneramr = calculation(gender=self.gender, weight=self.weight,
    #                                                          height=self.height,
    #                                                          age=self.age, sport=self.sport)
    #     self.showresult()
    #     self.amrexplanation()

    # def showresult(self):
    #     if amr > 0 and breakfastamr > 0 and lunchamr > 0 and dinneramr > 0:
    #         ttk.Label(self.frame1, text=f"Your AMR is {amr} calories per day.", anchor='sw', font=(30),
    #                   style="info").pack()
    #         ttk.Label(self.frame1, text=f"AMR for breakfast is {breakfastamr} calories.", anchor='sw', font=(30),
    #                   style="info").pack()
    #         ttk.Label(self.frame1, text=f"AMR for lunch is {lunchamr} calories.", anchor='sw', font=(30),
    #                   style="info").pack()
    #         ttk.Label(self.frame1, text=f"AMR for dinner is {dinneramr} calories.", anchor='sw', font=(30),
    #                   style="info").pack()
    #     else:
    #         ttk.Label(self.frame1, text="Please re-login and enter your personal information correctly.", anchor='sw',
    #                   font=(30),
    #                   style="info").pack()
    #     return
    #
    #     # amr explanation for frame2
    #
    # def amrexplanation(self):
    #     ttk.Label(self.frame2, text="AMR represents the amount of calories you need to consume each day to stay "
    #                                 "at your current weight.", anchor='sw', font=(30), style="info").pack()
    #     ttk.Label(self.frame2, text="AMR for breakfast and lunch are 35% of AMR per day, respectively.", anchor='sw',
    #               font=(30), style="info", width=200).pack()
    #     ttk.Label(self.frame2, text="AMR for dinner is 30% of AMR per day.", anchor='sw', font=(30), style="info",
    #               width=200).pack()
    #     return
    #
    def GoPage_three(self):
    #     self.page.destroy()
    #     self.notebook2.destroy()
    #     self.notebook1.destroy()
        pass


if __name__ == '__main__':
    window = tk.Tk()
    Page_one(master=window)
    Page_two(master=window)

    window.mainloop()
