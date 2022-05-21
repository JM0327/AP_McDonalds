from amrcalculation import *
from interface_1 import *


class AMRPage:

    def __init__(self, master, gointerface3):
        self.gointerface3 = gointerface3

        # user = InfoPage(self, gointerface2=None)
        # self.gender = user.inputgender.get()
        # self.height = user.inputheight.get()
        # self.weight = user.inputweight.get()
        # self.age = user.inputage.get()
        # self.sport = user.inputsport.get()

        self.gender = 0
        self.weight = 0
        self.height = 0
        self.age = 0
        self.sport = 0

        # here is creating the general window for interface
        style = ttk.Style(theme='darkly')
        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

        # Creat 2 notebook frame to put the amr result in
        # first one for amr result
        self.notebook1 = ttk.Notebook(self.page)
        self.notebook1.pack(pady=15,expand=True, anchor='n')
        self.frame1 = ttk.Frame(self.notebook1, width=450, height=150, style="dark")
        self.frame1.pack(fill='x', expand=True)
        self.frame1.pack_propagate(0)
        self.notebook1.add(self.frame1, text='Your AMR')

        # second one for amr explanation
        self.notebook2 = ttk.Notebook(self.page)
        self.notebook2.pack(pady=15, expand=True, anchor='n')
        self.frame2 = ttk.Frame(self.notebook2, width=450, height=150, style="dark")
        self.frame2.pack(fill='x', expand=True)
        self.frame2.pack_propagate(0)
        self.notebook2.add(self.frame2, text='Your AMR')

        # window structure
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').pack(side='right')
        ttk.Button(self.page, text='Next', command=self.bf_gointerface3, width=5,
                   style='success.TButton').pack(padx=10, side='right')

        # calculate amr to be used
        self.amr, self.breakfastamr, self.lunchamr, self.dinneramr = calculation(gender=self.gender, weight=self.weight,
                                                                                 height=self.height,
                                                                                 age=self.age, sport=self.sport)
        self.showresult()
        self.amrexplanation()

    # amr result for frame1
    def showresult(self):
        if self.amr > 0 and self.breakfastamr > 0 and self.lunchamr > 0 and self.dinneramr > 0:
            ttk.Label(self.frame1, text=f"Your AMR is {self.amr} calories per day.", anchor='sw', font=(40),
                      style="info", width=200).pack(pady=5)
            ttk.Label(self.frame1, text=f"AMR for breakfast is {self.breakfastamr} calories.", anchor='sw', font=(40),
                      style="info", width=200).pack(pady=5)
            ttk.Label(self.frame1, text=f"AMR for lunch is {self.lunchamr} calories.", anchor='sw', font=(40),
                      style="info", width=200).pack(pady=5)
            ttk.Label(self.frame1, text=f"AMR for dinner is {self.dinneramr} calories.", anchor='sw', font=(40),
                      style="info", width=200).pack(pady=5)
        else:
            ttk.Label(self.frame1, text="Please re-login and enter your personal information correctly.", anchor='sw',
                      font=(40), width=200, style="info").pack(pady=5)
        return

    # amr explanation for frame2
    def amrexplanation(self):
        ttk.Label(self.frame2, text="AMR represents the amount of calories you need or consume", anchor='sw', font=(40), style="info", width=200).pack(pady=5)
        ttk.Label(self.frame2, text="to consume each day to stay at your current weight.", anchor='sw', font=(40), style="info", width=200).pack()
        ttk.Label(self.frame2, text="AMR for breakfast is 35% of AMR per day, respectively.", anchor='sw',
                  font=(40), style="info", width=200).pack(pady=10)
        ttk.Label(self.frame2, text="AMR for lunch is 35% of AMR per day, respectively.", anchor='sw',
                  font=(40), style="info", width=200).pack(pady=5)
        ttk.Label(self.frame2, text="AMR for dinner is 30% of AMR per day.", anchor='sw', font=(40), style="info",
                  width=200).pack(pady=5)
        return

    def bf_gointerface3(self):
        self.notebook1.destroy()
        self.notebook2.destroy()
        self.page.destroy()
        self.gointerface3()



if __name__ == '__main__':
    window = tk.Tk()
    AMRPage(master=window, gointerface3=None)
    window.mainloop()
