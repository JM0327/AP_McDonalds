import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk
from interface3 import Recommendation


class AMR:
    def __init__(self, master):

        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Your Calories')
        self.window.geometry('500x500')

        self.page = tk.Frame(window)
        self.page.pack()

        ttk.Button(self.page, text='Next', command=Recommendation(self.page), style='success.TButton').grid(row=6, column=1, pady=30)



if __name__ == '__main__':
    window = tk.Tk()
    AMR(master=window)
    window.mainloop()