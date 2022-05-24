from Interface_2 import *
from tkinter import messagebox
import ttkbootstrap as ttk
from PIL import Image, ImageTk


class InfoPage:

    def __init__(self, master):
        """
        create window
        """
        style = ttk.Style(theme='flatly')

        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack(fill='both')

        """
        overall layout
        """
        self.frame1 = tk.Frame(self.page, width=500, height=50)
        self.frame2 = tk.Frame(self.page, width=500, height=450)
        self.frame21 = tk.Frame(self.frame2)
        self.frame22 = tk.Frame(self.frame2)
        self.frame23 = tk.Frame(self.frame2)
        self.frame24 = tk.Frame(self.frame2)
        self.frame25 = tk.Frame(self.frame2)
        self.frame26 = tk.Frame(self.frame2)
        self.frame1.pack(pady=20)
        self.frame2.pack()
        self.frame21.pack(fill='x', pady=10, anchor='n')
        self.frame22.pack(fill='x', pady=10, anchor='n')
        self.frame23.pack(fill='x', pady=10, anchor='n')
        self.frame24.pack(fill='x', pady=10, anchor='n')
        self.frame25.pack(fill='x', pady=10, anchor='n')
        self.frame26.pack(fill='x', pady=5, anchor='n')

        """
        logo
        """
        self.image = Image.open("../Application/Picture/McDonalds_logo.jpg")
        self.image = self.image.resize((154, 117), Image.ANTIALIAS)
        self.logo = ImageTk.PhotoImage(self.image)
        self.label_img = tk.Label(self.frame1, image=self.logo)
        self.label_img.pack(anchor='center')

        """
        personal information input
        """
        clickgender = ["Drop down",
                       "Female",
                       "Male"]
        clicksport = ["Drop down",
                      "Sedentary",
                      "Lightly active",
                      "Moderately active",
                      "Active",
                      "Very active"]

        self.inputgender = tk.StringVar()  # here is getting the info users put in
        self.inputweight = tk.StringVar()
        self.inputheight = tk.StringVar()
        self.inputage = tk.StringVar()
        self.inputsport = tk.StringVar()

        # creating a series of buttom and box that input the inforamtion

        ttk.Label(self.frame21, text='                  ') \
            .grid(row=0, column=0)
        ttk.Label(self.frame21, text='Gender: ', width=15) \
            .grid(row=0, column=1, padx=15, sticky='ne')
        ttk.OptionMenu(self.frame21, self.inputgender, *clickgender, style='dark-outline') \
            .grid(row=0, column=2, padx=20, sticky='nw')

        ttk.Label(self.frame22, text='                  ') \
            .grid(row=0, column=0, sticky='n')
        ttk.Label(self.frame22, text='Weight (unit:kg): ', width=15) \
            .grid(row=0, column=1, padx=15, sticky='ne')
        tk.Spinbox(self.frame22, from_=30, to=200, textvariable=self.inputweight, wrap=False, width=10) \
            .grid(row=0, column=2, padx=20, sticky='nw')

        ttk.Label(self.frame23, text='                  ') \
            .grid(row=0, column=0, sticky='n')
        ttk.Label(self.frame23, text='Height (unit:cm): ', width=15) \
            .grid(row=0, column=1, padx=15, sticky='ne')
        tk.Spinbox(self.frame23, from_=140, to=250, textvariable=self.inputheight, wrap=False, width=10) \
            .grid(row=0, column=2, padx=20, sticky='nw')

        ttk.Label(self.frame24, text='                  ') \
            .grid(row=0, column=0, sticky='n')
        ttk.Label(self.frame24, text='Age: ', width=15) \
            .grid(row=0, column=1, padx=15, sticky='ne')
        tk.Spinbox(self.frame24, from_=10, to=100, textvariable=self.inputage, wrap=False, width=10) \
            .grid(row=0, column=2, padx=20, sticky='nw')

        ttk.Label(self.frame25, text='                  ') \
            .grid(row=0, column=0, sticky='n')
        ttk.Label(self.frame25, text='Sport frequency: ', width=15) \
            .grid(row=0, column=1, padx=15, sticky='ne')
        ttk.OptionMenu(self.frame25, self.inputsport, *clicksport, style='dark-outline') \
            .grid(row=0, column=2, padx=20, sticky='nw')

        ttk.Button(self.frame26, text='Next', command=lambda: [self.gointerface2()], width=5, style='warning.TButton') \
            .grid(row=0, column=1, padx=200, pady=20)
        ttk.Label(self.frame26, text='          ') \
            .grid(row=1, column=1, sticky='n', pady=25)

        """
        go to next page if everything fill up
        """

    def gointerface2(self):

        gender = self.inputgender.get()
        weight = self.inputweight.get()
        height = self.inputheight.get()
        age = self.inputage.get()
        sport = self.inputsport.get()

        if gender == "female" or gender == "male" and sport == "Sedentary" or sport == "Lightly active" or sport == "Moderately active" or sport == "Active" or sport == "Very active":
            self.page.destroy()
            AMRPage(self.window, gender=gender, height=height, weight=weight, age=age, sport=sport)
        else:
            messagebox.showwarning(title='WARNING', message='Fail to entry, please check your information')

