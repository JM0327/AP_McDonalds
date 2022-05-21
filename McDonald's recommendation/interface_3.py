import tkinter as tk
import ttkbootstrap as ttk
from Optimization_problem import *
from amrcalculation import *


class Recommendation:
    def __init__(self, master):
        """
        create a window
        """
        style = ttk.Style(theme='darkly')
        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('500x500')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()
        """
        layout
        """
        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(anchor='s', pady=5, expand=True)
        self.frame1 = tk.Frame(self.notebook, width=480, height=500)
        self.frame2 = tk.Frame(self.notebook, width=480, height=500)
        self.frame3 = tk.Frame(self.notebook, width=480, height=500)
        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame1.pack_propagate(0)
        self.frame2.pack_propagate(0)
        self.frame3.pack_propagate(0)
        self.notebook.add(self.frame1, text='Breakfast choice')
        self.notebook.add(self.frame2, text='Lunch choice')
        self.notebook.add(self.frame3, text='Lunch choice')
        """
        result import
        """
        self.gender = gender
        self.weight = weight
        self.height = height
        self.age = age
        self.sport = sport
        self.amr, self.breakfastamr, self.lunchamr, self.dinneramr = calculation(gender=self.gender, weight=self.weight,
                                                                                 height=self.height,
                                                                                 age=self.age, sport=self.sport)
        self.breakfast_output, lunch_output, dinner_output = optimization_meal(breakfastamr=self.breakfastamr,
                                                                               lunchamr=self.lunchamr,
                                                                               dinneramr=self.dinneramr)

        def breakfast(self):
            ttk.Label(self.frame2, text="AMR represents the amount of calories you need or consume", anchor='sw',
                      font=(40), style="info", width=200).pack(pady=5)
            ttk.Label(self.frame2, text="to consume each day to stay at your current weight.", anchor='sw', font=(40),
                      style="info", width=200).pack()
            ttk.Label(self.frame2, text="AMR for breakfast is 35% of AMR per day, respectively.", anchor='sw',
                      font=(40), style="info", width=200).pack(pady=10)
            ttk.Label(self.frame2, text="AMR for lunch is 35% of AMR per day, respectively.", anchor='sw',
                      font=(40), style="info", width=200).pack(pady=5)
            ttk.Label(self.frame2, text="AMR for dinner is 30% of AMR per day.", anchor='sw', font=(40), style="info",
                      width=200).pack(pady=5)


if __name__ == '__main__':
    window = tk.Tk()
    Recommendation(master=window)
    window.mainloop()
