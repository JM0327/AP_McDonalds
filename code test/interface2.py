import tkinter as tk
from doctest import master
from tkinter import messagebox
import ttkbootstrap as ttk


class AMRPage:
    def __init__(self, master):
        # here is creating the general window for interface
        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Your Calories')
        self.window.geometry('650x650')  # size

        # here is the notebook frame for showing the recommendation
        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(anchor='s', pady=50, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook, width=600, height=350)
        self.frame3 = tk.Frame(self.notebook, width=600, height=350)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        self.notebook.add(self.frame1, text='Breakfast choice')
        self.notebook.add(self.frame2, text='Lunch choice')
        self.notebook.add(self.frame3, text='Lunch choice')

        # here is creating the Meals option check box






if __name__ == '__main__':
    window = tk.Tk()
    AMRPage(master=window)
    window.mainloop()
