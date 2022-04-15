import re
import sys

# input basic information

print("Please enter your personal information!")

gender = input("please enter your gender ( male or female):")
if not re.match('male|female', gender):
    print("Error! Only letters male or female allowed!")
    sys.exit()

weight = float(input("please enter your weight (unit: kg):"))
if weight <0 or weight > 300:
    print("Error! Only the weight between 0 and 300 allowed!")
    sys.exit()

height = float(input("please enter your height (unit: cm):"))
if height <100 or height > 999:
    print("Error! Only 3 characters allowed!")
    sys.exit()

age = int(input("please enter your age:"))
if age <0 or age >100:
    print("Error! Only 2 characters allowed!")
    sys.exit()

# calculate bmr

if gender == "male":
    bmr = 13.7 * weight + 5.0 * height - 6.8 * age + 66
elif gender == "female":
    bmr = 9.6 * weight + 3.8 * height - 4.7 * age + 655
else:
    bmr = -1

# input the frequency of doing sport

print("""
How frequent do you do sport?
Sedentary (little or no exercise)：please enter 1 below
Lightly active (exercise 1–3 days/week)：please enter 2 below
Moderately active (exercise 3–5 days/week)：please enter 3 below
Active (exercise 6–7 days/week)：please enter 4 below
Very active (hard exercise 6–7 days/week)：please enter 5 below
""")

frequency = input("Please follow the prompts above to enter your exercise frequency:")
sport = int(frequency)

if sport!=1 and sport!=2 and sport!=3 and sport!=4 and sport!=5:
    print("Error! Only number 1,2,3,4,5 allowed!")
    sys.exit()

# calculate AMR

try:
    if bmr != -1:
        if sport == 1:
            amr = round(bmr * 1.2, 2)
        elif sport == 2:
            amr = round(bmr*1.375, 2)
        elif sport == 3:
            amr = round(bmr * 1.55, 2)
        elif sport == 4:
            amr = round(bmr * 1.725, 2)
        else:
            amr = round(bmr * 1.9, 2)
    else:
        print("Please check your personal information!")

except ValueError:
    print("Please enter your personal information correctly!")
except IndexError:
    print("Please enter your personal information completely！")
except:
    print("error!")

print(f"Your AMR is {amr} calories per day.")
print("AMR represents the number of calories you need to consume each day to stay at your current weight.")