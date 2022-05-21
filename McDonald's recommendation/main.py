from interface_2 import *
from interface_3 import *


class Run:

    def __init__(self):
        style = ttk.Style(theme='darkly')

        self.window = style.master
        self.window.title('McDonalds')
        self.window.geometry('500x500')  # size

        self.page = tk.Frame(self.window)
        self.page.pack()

        self.gointerface1()

    def gointerface1(self):
        self.page.destroy()
        InfoPage(self, gointerface2=self.gointerface2)

    def gointerface2(self):
        self.page.destroy()
        AMRPage(self, gointerface3= self.gointerface3)
    #
    def gointerface3(self):
        self.page.destroy()
        Recommendation(self)



if __name__ == "__main__":
    window = tk.Tk()
    Run()
    window.mainloop()
