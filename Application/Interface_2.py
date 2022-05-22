from AMRCalculation import *
from Interface_3 import *


class AMRPage:

    def __init__(self, master, gender, height, weight, age, sport):

        self.gender = gender
        self.height = height
        self.weight = weight
        self.age = age
        self.sport = sport

        # here is creating the general window for interface
        style = ttk.Style(theme='flatly')
        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

        # Creat 2 notebook frame to put the amr result in
        # first one for amr result
        self.notebook1 = ttk.Notebook(self.page, style='default')
        self.notebook1.pack(pady=15, expand=True, anchor='n')
        self.frame1 = ttk.Frame(self.notebook1, width=450, height=150, style="default")
        self.frame1.pack(fill='x', expand=True)
        self.frame1.pack_propagate(0)
        self.notebook1.add(self.frame1, text='Your AMR')

        # second one for amr explanation
        self.notebook2 = ttk.Notebook(self.page, style='default')
        self.notebook2.pack(pady=15, expand=True, anchor='n')
        self.frame2 = ttk.Frame(self.notebook2, width=450, height=150, style="default")
        self.frame2.pack(fill='x', expand=True)
        self.frame2.pack_propagate(0)
        self.notebook2.add(self.frame2, text='Your AMR')

        # window structure
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').pack(side='right')
        ttk.Button(self.page, text='Next', command=self.gointerface3, width=5,
                   style='success.TButton').pack(padx=10, side='right')

        self.amr, self.breakfastamr, self.lunchamr, self.dinneramr = amrcalculation(gender=self.gender,
                                                                                    weight=self.weight,
                                                                                    height=self.height,
                                                                                    age=self.age,
                                                                                    sport=self.sport)

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
        explanation1 = "AMR represents the amount of calories you need or consume to consume " \
                       "each day to stay at your current weight."
        explanation2 = "AMR for breakfast occupies 35% of AMR per day, respectively."
        explanation3 = "AMR for lunch occupies 35% of AMR per day, respectively."
        explanation4 = "AMR for dinner occupies 30% of AMR per day."

        tk.Message(self.frame2, text=explanation1, width=440, anchor='w', justify='left', bg='white').pack(pady=5, anchor='w',fill='x')
        tk.Message(self.frame2, text=explanation2, width=440, anchor='w', justify='left', bg='white').pack(pady=2, anchor='w',fill='x')
        tk.Message(self.frame2, text=explanation3, width=440, anchor='w', justify='left', bg='white').pack(pady=2, anchor='w',fill='x')
        tk.Message(self.frame2, text=explanation4, width=440, anchor='w', justify='left', bg='white').pack(pady=2, anchor='w',fill='x')



    def gointerface3(self):
        self.notebook1.destroy()
        self.notebook2.destroy()
        self.page.destroy()
        Recommendation(self.window, amr= self.amr, breakfastamr=self.breakfastamr, lunchamr=self.lunchamr, dinneramr=self.dinneramr)



