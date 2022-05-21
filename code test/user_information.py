from interface_1 import *


class User:

    def __int__(self):
        saveinfo = InfoPage(self)
        self.gender = saveinfo.inputgender.get()
        self.weight = saveinfo.inputweight.get()
        self.height = saveinfo.inputheight.get()
        self.age = saveinfo.inputage.get()
        self.sport = saveinfo.inputsport.get()

        return self


if __name__ == '__main__':
    User()
