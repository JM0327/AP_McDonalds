import tkinter as tk
from tkinter import messagebox
import ttkbootstrap as ttk


class Recommendation:
    def __init__(self, master):

        #style = ttk.Style(theme='darkly')

        self.window = master
        #self.window = style.master
        self.window.title('Choices for you')
        self.window.geometry('500x500')  # size

        ttk.Button(self.window, text='Breakfast', style='success.TButton', command=self.recommenddish,
                   width=10).place(x=30, y=20)
        ttk.Button(self.window, text='Lunch', style='success.TButton', command=self.recommenddish,
                   width=10).place(x=180, y=20)
        ttk.Button(self.window, text='Dinner', style='success.TButton', command=self.recommenddish,
                   width=10).place(x=330, y=20)

    def recommenddish(self):
        pass








if __name__ == '__main__':
    window = tk.Tk()
    Recommendation(window)
    window.mainloop()