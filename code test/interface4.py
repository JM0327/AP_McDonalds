import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk

# first choice without nutrition restriction

class Optimization1:
    def __init__(self, master):

        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Choice for you')
        self.window.geometry('500x500')  # size

if __name__ == '__main__':
    window = tk.Tk()
    Calories(master=window)
    window.mainloop()  # we must have loop.