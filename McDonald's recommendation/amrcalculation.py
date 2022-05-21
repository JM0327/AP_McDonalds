

def calculation(gender, weight, height, age, sport):
    if not gender is None and not weight is None and not height is None and not age is None and not sport is None:
        if gender == "male":
            bmr = 13.75 * int(weight) + 5.003 * int(height) - 6.755 * int(age) + 66.47
        else:
            bmr = 9.563 * int(weight) + 1.850 * int(height) - 4.676 * int(age) + 655.1

        if sport == "Sedentary":
            amr = round(bmr * 1.2, 2)
        elif sport == "Lightly active":
            amr = round(bmr * 1.375, 2)
        elif sport == "Moderately active":
            amr = round(bmr * 1.55, 2)
        elif sport == "Active":
            amr = round(bmr * 1.725, 2)
        else:
            amr = round(bmr * 1.9, 2)
    else:
        amr = 0

    if amr > 0:
        breakfastamr = int(amr * 0.35)
        lunchamr = int(amr * 0.35)
        dinneramr = int(amr * 0.30)
    else:
        breakfastamr = 0
        lunchamr = 0
        dinneramr = 0

    return amr, breakfastamr, lunchamr, dinneramr
