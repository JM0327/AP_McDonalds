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

        self.page = tk.Frame(self.window)
        self.page.pack()

        # here is the notebook frame for showing the recommendation
        self.notebook = ttk.Notebook(style.master)
        self.notebook.pack(anchor='s', pady=50, expand=True)

        self.frame1 = tk.Frame(self.notebook)
        self.frame2 = tk.Frame(self.notebook, width=600, height=350)
        self.frame3 = tk.Frame(self.notebook, width=600, height=350)

        self.frame1.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame2.pack(fill='both', expand=True)
        self.frame1.pack_propagate(0)
        self.frame2.pack_propagate(0)
        self.frame3.pack_propagate(0)

        self.notebook.add(self.frame1, text='Breakfast choice')
        self.notebook.add(self.frame2, text='Lunch choice')
        self.notebook.add(self.frame3, text='Lunch choice')

        # here is getting the choice of users choosing meals
        self.breakfastchoice = tk.IntVar()
        self.lunchchoice = tk.IntVar()
        self.dinnerchoice = tk.IntVar()

        # here is creating the Meals option check box
        tk.Checkbutton(self.page, text="Click this box, if you want to eat McDonald's for breakfast!",
                       variable=self.breakfastchoice).grid(row=1, column=1, sticky='w', padx=0, pady=15)
        tk.Checkbutton(self.page, text="Click this box, if you want to eat McDonald's for lunch!",
                       variable=self.lunchchoice).grid(row=2, column=1, sticky='w', padx=0, pady=15)
        tk.Checkbutton(self.page, text="Click this box, if you want to eat McDonald's for dinner!",
                       variable=self.dinnerchoice).grid(row=3, column=1, sticky='w', padx=0, pady=15)
        tk.Label(self.page, text="                            ").grid(row=0, column=2, sticky='w', padx=0, pady=10) # dummy column
        tk.Label(self.page, text="                            ").grid(row=0, column=3, sticky='w', padx=0, pady=10) # dummy column



    # code for optimization
    def recommendation(self):

        global breakfastchoice, lunchchoice, dinnerchoice
        # get the choice that users click, it will be 0/1

        breakfastchoice = self.breakfastchoice.get()
        lunchchoice = self.lunchchoice.get()
        dinnerchoice = self.dinnerchoice.get()

        pass

    # create a popup window that can initiate the display of optimization recommendation
    # haven't finished, it should be linked with the optimization part
    def popup(self):

        breakfastchoice = self.breakfastchoice.get()
        lunchchoice = self.lunchchoice.get()
        dinnerchoice = self.dinnerchoice.get()


        if not breakfastchoice is None or not lunchchoice is None or not dinnerchoice is None :
            response = messagebox.askquestion("Q", "Do you want to find your recommendation dishes?")
            if response == "yes":
                pass
            else:
                ttk.Label(self.frame1, text="oops! you haven't chosen.", style="dark").pack()
                ttk.Label(self.frame2, text="oops! you haven't chosen.", style="dark").pack()
                ttk.Label(self.frame3, text="oops! you haven't chosen.", style="dark").pack()

        else:
            messagebox.showwarning(title='WARNING', message='Fail to show, please click which meal you want.')







if __name__ == '__main__':
    window = tk.Tk()
    AMRPage(master=window)
    window.mainloop()
