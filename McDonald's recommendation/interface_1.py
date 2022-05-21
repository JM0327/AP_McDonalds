import tkinter as tk
import ttkbootstrap as ttk
from basic_information import *



class InfoPage:

    def bf_gointerface2(self):
        self.gointerface2()

    def __init__(self, master, gointerface2):
        self.gointerface2 = gointerface2

        # here is creating the general window for interface
        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

        # Drop Down box content, call information from basic information file
        self.genderclick = basicinfo.clickgender  # information choice
        self.sportclick = basicinfo.clicksport  # information choice
        self.inputgender = tk.StringVar()# here is getting the info users put in
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()

        # here is creating a series of buttom and box that input the inforamtion
        tk.Label(self.page).grid(row=0, column=0)

        tk.Label(self.page, text='Gender(male/female): ', anchor="nw", width=15).grid(row=1, column=0, pady=25)
        ttk.OptionMenu(self.page, self.inputgender, *self.genderclick, style="dark").grid(row=1, column=2)

        tk.Label(self.page, text='Weight(unit:kg): ', anchor="nw", width=15).grid(row=2, column=0, pady=25)
        tk.Spinbox(self.page, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=10).grid(row=2,
                                                                                                          column=2)

        tk.Label(self.page, text='Height(unit:cm): ', anchor="nw", width=15).grid(row=3, column=0, pady=25)
        tk.Spinbox(self.page, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=10).grid(row=3,
                                                                                                           column=2)

        tk.Label(self.page, text='Age(integer): ', anchor="nw", width=15).grid(row=4, column=0, pady=25)
        tk.Spinbox(self.page, from_=10, to=100, textvariable=self.inputage, wrap=False, width=10).grid(row=4, column=2)

        tk.Label(self.page, text='Sport frequency: ', anchor="nw", width=15).grid(row=5, column=0, pady=25)
        ttk.OptionMenu(self.page, self.inputsport, *self.sportclick, style="dark").grid(row=5, column=2)

        tk.Label(self.page, text='     ').grid(row=6, column=1, pady=5)  # dummy column
        tk.Label(self.page, text=' ').grid(row=6, column=6, pady=5)  # dummy column

        ttk.Button(self.page, text='Next', command=lambda: [self.destroypage(), self.bf_gointerface2()], width=5,
                   style='success.TButton').grid(row=7, column=4)
        ttk.Button(self.page, text='Quit', command=self.page.quit, width=5, style='success.TButton').grid(row=7,
                                                                                                          column=7)

    def destroypage(self):
        self.page.destroy()

if __name__ == '__main__':
    window = tk.Tk()
    InfoPage(master=window, gointerface2=None)
    window.mainloop()
