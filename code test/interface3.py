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
        self.CreatePage()

    def callback():
        print("~被调用啦~")

    def CreatePage(self):
        menubar = tk.Menu(self.window)

        menubar.add_command(label='Breakfast', command=self.callback)
        menubar.add_command(label='Lunch')
        menubar.add_command(label='Dinner')
        self.window['menu']=menubar






if __name__ == '__main__':
    window = tk.Tk()
    Recommendation(window)
    window.mainloop()