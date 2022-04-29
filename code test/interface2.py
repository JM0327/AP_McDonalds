import tkinter as tk
from tkinter import messagebox
import re
import sys

class Calories:
    def __init__(self, master):

        self.window = master
        self.window.title('Choice for you')
        self.window.geometry('500x500')  # size

if __name__ == '__main__':
    window = tk.Tk()
    Calories(master=window)
    window.mainloop()  # we must have loop.

