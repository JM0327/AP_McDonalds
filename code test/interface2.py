import tkinter as tk
from doctest import master
from tkinter import messagebox
import ttkbootstrap as ttk


class AMRPage:
    def __init__(self, master):
        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Your Calories')
        self.window.geometry('650x650')  # size

        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(pady=10, expand=True)

        self.frame1 = tk.Frame(self.notebookc)
        self.frame2 = tk.Frame(self.notebook, width=600, height=600)
        self.frame3 = tk.Frame(self.notebook, width=600, height=600)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)

        self.notebook.add(self.frame1, text='Breakfast choice')
        self.notebook.add(self.frame2, text='Lunch choice')
        self.notebook.add(self.frame3, text='Lunch choice')






if __name__ == '__main__':
    window = tk.Tk()
    AMRPage(master=window)
    window.mainloop()
