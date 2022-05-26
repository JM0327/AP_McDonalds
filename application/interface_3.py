import tkinter as tk
import ttkbootstrap as ttk
from optimization_calculation import *
from nutrition_plot import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk  # NavigationToolbar2TkAgg


class Recommendation:
    def __init__(self, master, amr, breakfastamr, lunchamr, dinneramr):
        """
        create a window
        """
        style = ttk.Style(theme='flatly')
        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('500x550')  # size
        self.page = tk.Frame(self.window)
        self.page.pack()
        """
        layout
        one notebook
            - frame 1 -> eg. for one meal one
                - frame1.1 -> for showing result
                - frame1.2 -> for plotting
        """
        self.notebook = ttk.Notebook(self.window, style='warning', height=450)
        self.notebook.pack(anchor='s', pady=5, expand=True)

        self.frame1 = tk.Frame(self.notebook, width=480, height=450)
        self.frame11 = tk.Frame(self.frame1, width=480, height=120)
        self.frame12 = tk.Frame(self.frame1, width=480, height=330)
        self.frame1.pack(fill='both', expand=True)
        self.frame11.pack(fill='x', anchor='n', pady=5)
        self.frame12.pack(fill='x', anchor='s')
        self.frame1.pack_propagate(0)
        self.frame11.pack_propagate(0)
        self.frame12.pack_propagate(0)

        self.frame2 = tk.Frame(self.notebook, width=480, height=450)
        self.frame21 = tk.Frame(self.frame2, width=480, height=120)
        self.frame22 = tk.Frame(self.frame2, width=480, height=330)
        self.frame2.pack(fill='both', expand=True)
        self.frame21.pack(fill='x', expand=True, anchor='n', pady=5)
        self.frame22.pack(fill='x', expand=True, anchor='s')
        self.frame2.pack_propagate(0)
        self.frame21.pack_propagate(0)
        self.frame22.pack_propagate(0)

        self.frame3 = tk.Frame(self.notebook, width=480, height=450)
        self.frame31 = tk.Frame(self.frame3, width=480, height=120)
        self.frame32 = tk.Frame(self.frame3, width=480, height=330)
        self.frame3.pack(fill='both', expand=True)
        self.frame31.pack(fill='x', expand=True, anchor='n', pady=5)
        self.frame32.pack(fill='x', expand=True, anchor='s')
        self.frame3.pack_propagate(0)
        self.frame31.pack_propagate(0)
        self.frame32.pack_propagate(0)


        self.notebook.add(self.frame1, text='Breakfast choice')
        self.notebook.add(self.frame2, text='Lunch choice')
        self.notebook.add(self.frame3, text='Dinner choice')
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
        """
        create a canvas
        """
        self.canvas1 = tk.Canvas()
        self.figure1 = self.breakfast_plot()
        self.figure1_form(self.figure1)

        self.canvas2 = tk.Canvas()
        self.figure2 = self.lunch_plot()
        self.figure2_form(self.figure2)

        self.canvas3 = tk.Canvas()
        self.figure3 = self.dinner_plot()
        self.figure3_form(self.figure3)

        """
        run following function
        """
        self.breakfast()
        self.lunch()
        self.dinner()

        """
        quit window
        """
        self.frame0 = tk.Frame(self.window, width=480, height=50)
        self.frame0.pack(fill='x', expand=True, anchor='s')
        self.frame0.pack_propagate(0)

        ttk.Button(self.frame0, text='Quit', command=self.page.quit, width=5, style='warning.TButton') \
            .pack(side='right', padx=10)

        """
        showing result function
        """
    def breakfast(self):
        b = self.breakfast_output['name']
        breakfastdish = "\n".join(b)
        tk.Message(self.frame11, text=breakfastdish, width=400, anchor='w', justify='left', bg='white').pack(
            pady=10, padx=10, anchor='w', fill='x')

    def lunch(self):
        l = self.lunch_output['name']
        lunchdish = "\n".join(l)
        tk.Message(self.frame21, text=lunchdish, width=400, anchor='w', justify='left', bg='white').pack(
            pady=10, padx=10, anchor='w', fill='x')

    def dinner(self):
        d = self.dinner_output['name']
        dinnerdish = "\n".join(d)
        tk.Message(self.frame31, text=dinnerdish, width=400, anchor='w', justify='left', bg='white').pack(
            pady=10, padx=10, anchor='w', fill='x')

        """
        plotting function
        """

    def breakfast_plot(self):
        breakfastplot = meal_plot(optimization_output=self.breakfast_output, mealamr=self.breakfastamr, ratio=0.35)
        return breakfastplot

    def figure1_form(self, figure):
        self.canvas1 = FigureCanvasTkAgg(figure, self.frame12)
        self.canvas1.draw()
        self.canvas1.get_tk_widget().pack(fill='y')
        toolbar = NavigationToolbar2Tk(self.canvas1, self.frame12)
        toolbar.update()
        self.canvas1._tkcanvas.pack()

    def lunch_plot(self):
        lunchplot = meal_plot(optimization_output=self.lunch_output, mealamr=self.lunchamr, ratio=0.35)
        return lunchplot

    def figure2_form(self, figure):
        self.canvas2 = FigureCanvasTkAgg(figure, self.frame22)
        self.canvas2.draw()
        self.canvas2.get_tk_widget().pack(fill='y')
        toolbar = NavigationToolbar2Tk(self.canvas2, self.frame22)
        toolbar.update()
        self.canvas2._tkcanvas.pack()

    def dinner_plot(self):
        dinnerplot = meal_plot(optimization_output=self.dinner_output, mealamr=self.dinneramr, ratio=0.30)
        return dinnerplot

    def figure3_form(self, figure):
        self.canvas3 = FigureCanvasTkAgg(figure, self.frame32)
        self.canvas3.draw()
        self.canvas3.get_tk_widget().pack(fill='y')
        toolbar = NavigationToolbar2Tk(self.canvas3, self.frame32)
        toolbar.update()
        self.canvas3._tkcanvas.pack()
