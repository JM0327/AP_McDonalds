import numpy as np
from matplotlib import pyplot as plt


def breakfast_plot(breakfast_output, breakfastamr):

    columns = ["Calories", "Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Sugars"]
    color_choose = ['lightcoral', 'darkorange', 'plum', 'palegreen', 'skyblue', 'paleturquoise']# color the bar plot

    dish_values = []
    for key in breakfast_output.keys():
        add_value1 = breakfast_output[key]
        dish_values.append(add_value1)
    dish_values = dish_values[2:8]
    print(dish_values)

    for i in range(6):
        if i == 0:
            dish_values[i] = dish_values[i] * 100 / breakfastamr
        else:
            dish_values[i] = dish_values[i] / 0.35
    x_axis = range(len(columns))
    plt.bar(x_axis, dish_values, width=0.4, color=color_choose)
    plt.xticks(x_axis, columns)
    plt.yticks(np.arange(0, 110, 10))
    plt.ylabel("percentage")
    plt.title("The nutrition provided by McDonald's breakfast\n(% of total meal nutrition needed)")
    b_y_max = max(dish_values) + max(dish_values) / 6
    for x, y in enumerate(dish_values):
        plt.text(x, y + b_y_max / 100, str(round(dish_values[x], 1)) + "%", ha="center")
    plt.savefig('../Plot/breakfast_plot.jpg')




# def graph(optimization_output):
#         columns = ["Calories", "Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Sugars"]
#         color_choose = ['lightcoral', 'darkorange', 'plum', 'palegreen', 'skyblue', 'paleturquoise']
#         # color the bar plot
#
#         dish_values = []
#         for key in optimization_output.keys():
#             add_value1 = optimization_output[key]
#             dish_values.append(add_value1)
#         dish_values = dish_values[2:8]
#         print(dish_values)
#
#         if optimization_output == breakfast_output:
#             for i in range(6):
#                 if i == 0:
#                     dish_values[i] = dish_values[i] * 100 / breakfastamr
#                 else:
#                     dish_values[i] = dish_values[i] / 0.35
#             x_axis = range(len(columns))
#             plt.bar(x_axis, dish_values, width=0.4, color=color_choose)
#             plt.xticks(x_axis, columns)
#             plt.yticks(np.arange(0, 110, 10))
#             plt.ylabel("percentage")
#             plt.title("The nutrition provided by McDonald's breakfast\n(% of total meal nutrition needed)")
#             b_y_max = max(dish_values) + max(dish_values) / 6
#             for x, y in enumerate(dish_values):
#                 plt.text(x, y + b_y_max / 100, str(round(dish_values[x], 1)) + "%", ha="center")
#             plt.savefig('./breakfast_plot.jpg')
#
#         elif optimization_output == lunch_output:
#             for i in range(6):
#                 if i == 0:
#                     dish_values[i] = dish_values[i] * 100 / lunchamr
#                 else:
#                     dish_values[i] = dish_values[i] / 0.35
#             x_axis = range(len(columns))
#             plt.bar(x_axis, dish_values, width=0.4, color=color_choose)
#             plt.xticks(x_axis, columns)
#             plt.yticks(np.arange(0, 110, 10))
#             plt.ylabel("percentage")
#             plt.title("The nutrition provided by McDonald's lunch\n(% of total meal nutrition needed)")
#             b_y_max = max(dish_values) + max(dish_values) / 6
#             for x, y in enumerate(dish_values):
#                 plt.text(x, y + b_y_max / 100, str(round(dish_values[x], 1)) + "%", ha="center")
#             plt.savefig('./lunch_plot.jpg')
#
#         elif optimization_output == dinner_output:
#             for i in range(6):
#                 if i == 0:
#                     dish_values[i] = dish_values[i] * 100 / dinneramr
#                 else:
#                     dish_values[i] = dish_values[i] / 0.3
#             x_axis = range(len(columns))
#             plt.bar(x_axis, dish_values, width=0.4, color=color_choose)
#             plt.xticks(x_axis, columns)
#             plt.yticks(np.arange(0, 110, 10))
#             plt.ylabel("percentage")
#             plt.title("The nutrition provided by McDonald's meal\n(% of total meal nutrition needed)")
#             b_y_max = max(dish_values) + max(dish_values) / 6
#             for x, y in enumerate(dish_values):
#                 plt.text(x, y + b_y_max / 100, str(round(dish_values[x], 1)) + "%", ha="center")
#             plt.savefig('./dinner_plot.jpg')
#
#
#     # graph(breakfast_output)
#     # graph(lunch_output)
#     # graph(dinner_output)
