import tkinter as tk
from tkinter import messagebox
import re
import sys
from interface2 import Calories
import pandas as pd

#sys.path.append('../calculation/')
#import BMR_AMR

class InfoPage:

    def __init__(self, master):

        self.window = master
        self.window.title('Personal Information')
        self.window.geometry('600x400')  # size

        self.inputgender = tk.StringVar()
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self. inputage = tk.StringVar()

        self.page = tk.Frame(window)
        self.page.pack()

        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='Gender(male/female): ').grid(row=1, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.inputgender).grid(row=1, column=2)

        tk.Label(self.page, text='Weight(unit:kg): ').grid(row=2, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.inputweight).grid(row=2, column=2)

        tk.Label(self.page, text='Height(unit:cm): ').grid(row=3, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.inputheight).grid(row=3, column=2)

        tk.Label(self.page, text='Age(integer): ').grid(row=4, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.inputage).grid(row=4, column=2)

        tk.Button(self.page, text='Calculate', command=self.info).grid(row=5, column=1, pady=30)
        tk.Button(self.page, text='Quit', command=self.page.quit).grid(row=5, column=3)

    def info(self):
        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self. inputage.get()
        if re.match('male|female', gender) or weight > 0 or weight < 300 or height > 100 or height < 999 or age > 0 or age < 100:
            # what restriction we should define?
            self.page.destroy()
            Calories(self.page)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')

    def saveinfo(self):
        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        dict = {'gender': gender, 'weight':weight, 'height':height, 'age': age }
        infodf = pd.DataFrame(dict)

if __name__ == '__main__':
    window = tk.Tk()
    InfoPage(master=window)
    window.mainloop()  # we must have loop.


