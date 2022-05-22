import tkinter as tk
import ttkbootstrap as ttk
from Optimization_problem import *
from Nutrition_plot import *
from matplotlib.figure import Figure


class Recommendation:
    def __init__(self, master, amr, breakfastamr, lunchamr, dinneramr):
        """
        create a window
        """
        style = ttk.Style(theme='flatly')
        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('500x500')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()
        """
        layout
        """
        self.notebook = ttk.Notebook(style.master, style='info', height= 450)
        self.notebook.pack(anchor='s', pady=5, expand=True)
        self.frame1 = tk.Frame(self.notebook, width=480, height=450)
        self.frame2 = tk.Frame(self.notebook, width=480, height=450)
        self.frame3 = tk.Frame(self.notebook, width=480, height=450)
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
        self.amr = amr
        self.breakfastamr = breakfastamr
        self.lunchamr = lunchamr
        self.dinneramr = dinneramr
        self.breakfast_output, self.lunch_output, self.dinner_output = optimization_meal(breakfastamr=self.breakfastamr,
                                                                                         lunchamr=self.lunchamr,
                                                                                         dinneramr=self.dinneramr)
        self.cv = tk.Canvas(self.page, bg='white')

        """
        run following function
        """
        self.breakfast()
        self.lunch()
        self.dinner()
        breakfast_plot(self.breakfast_output, self.breakfastamr)
        self.breakfast_plot()

    def breakfast(self):
        breakfastdish = self.breakfast_output['name']
        tk.Message(self.frame1, text=breakfastdish, width=450, anchor='sw', justify='left', bg='white').pack(pady=5, anchor='w',fill='x')

    def lunch(self):
        breakfastdish = self.lunch_output['name']
        tk.Message(self.frame2, text=breakfastdish, width=450, anchor='sw', justify='left',bg='white').pack(pady=5, anchor='w',fill='x')

    def dinner(self):
        breakfastdish = self.dinner_output['name']
        tk.Message(self.frame3, text=breakfastdish, width=450, anchor='sw', justify='left',bg='white').pack(pady=5, anchor='w',fill='x')

    def breakfast_plot(self):
        img = tk.PhotoImage(file="../Plot/breakfast_plot.jpg")
        self.cv.create_image(30,150, image=img, anchor='s')
        self.cv.pack()
