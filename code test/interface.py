import tkinter as tk
from tkinter import messagebox
import re
from interface2 import AMR
import ttkbootstrap as ttk

class InfoPage:

    def __init__(self, master):

        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('Personal Information')
        self.window.geometry('650x500')  # size


        self.inputgender = tk.StringVar()
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()

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

        tk.Label(self.page, text='Sport frequency: ').grid(row=5, column=1, pady=20)
        tk.Entry(self.page, textvariable=self.inputsport).grid(row=5, column=2)

        ttk.Button(self.page, text='Calculate', command=self.info, style='success.TButton').grid(row=6, column=1, pady=30)
        ttk.Button(self.page, text='Quit', command=self.page.quit, style='success.TButton').grid(row=6, column=3)

    def info(self):
        self.gender = self.inputgender.get()
        self.weight = self.inputweight.get()
        self.height = self.inputheight.get()
        self.age = self. inputage.get()
        self.sport = self.inputsport.get()
        if re.match('male|female', self.gender) or \
                self.weight > 0 or self.weight < 300 or \
                self.height > 100 or self.height < 999 or \
                self.age > 0 or self.age < 100:
            print(self.gender, self.weight, self.height, self.age, self.sport)
            self.page.destroy()
            AMR(self.page)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')
        return


if __name__ == '__main__':
    window = tk.Tk()
    InfoPage(master=window)
    window.mainloop()

