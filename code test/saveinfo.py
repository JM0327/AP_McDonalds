
class AllInfo:

    def __init__(self, infoinput):
        self.information = []
        self.information.extend(infoinput)

    def saveinfo(self):
        if len(self.information) > 0:
            information = self.information
            print(information)

    def bmramr(self):
        if self.information[0] == "male":
            bmr = 13.7 * self.information[1] + 5.0 * self.information[2] - 6.8 * self.information[3] + 66
        else:
            bmr = 9.6 * self.information[1] + 3.8 * self.information[2] - 4.7 * self.information[3] + 655

        if self.information[4] == "Sedentary":
            amr = round(bmr * 1.2, 2)
        elif self.information[4] == "Lightly active":
            amr = round(bmr * 1.375, 2)
        elif self.information[4] == "Moderately active":
            amr = round(bmr * 1.55, 2)
        elif self.information[4] == "Active":
            amr = round(bmr * 1.725, 2)
        else:
            amr = round(bmr * 1.9, 2)


        print(f"Your AMR is {amr} calories per day.")
        print("AMR is effectively the number of calories that we consume on a daily basis depending on our height, "
              "sex, age, weight and entered activity level whilst maintaining current weight.")

        breakfestamr = round(amr*0.35, 2)
        lunchamr = round(amr*0.35, 2)
        dinneramr = round(amr*0.30, 2)

        print(f"Your AMR for Breakfast is {breakfestamr} calories.")
        print(f"Your AMR for Lunch is {lunchamr} calories.")
        print(f"Your AMR for Dinner is {dinneramr} calories.")







if __name__ == '__main__':
    AllInfo()
