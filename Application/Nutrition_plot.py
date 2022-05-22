import numpy as np
from matplotlib import pyplot as plt


def meal_plot(optimization_output, mealamr):
    """
    basic information
    """
    columns = ["Calories", "Total Fat", "Saturated Fat", "Cholesterol", "Sodium", "Sugars"]
    color_choose = ['slategray', 'lightsteelblue', 'steelblue', 'lightslategray', 'cadetblue','powderblue']  # color the bar plot
    """
    plotting
    """
    plot = plt.figure(figsize=(7, 7), dpi=70)
    figure = plt.subplot(1, 1, 1)

    dish_values = []
    for key in optimization_output.keys():
        add_value1 = optimization_output[key]
        dish_values.append(add_value1)
    dish_values = dish_values[2:8]
    print(dish_values)

    for i in range(6):
        if i == 0:
            dish_values[i] = dish_values[i] * 100 / mealamr
        else:
            dish_values[i] = dish_values[i] / 0.35
    x_axis = range(len(columns))
    plt.bar(x_axis, dish_values, width=0.4, color=color_choose)
    figure.set_xticks(x_axis, columns)
    figure.set_yticks(np.arange(0, 110, 10))
    figure.set_ylabel("percentage")
    plt.title("The nutrition provided by McDonald's breakfast\n(% of total meal nutrition needed)")
    b_y_max = max(dish_values) + max(dish_values) / 6
    for x, y in enumerate(dish_values):
        plt.text(x, y + b_y_max / 100, str(round(dish_values[x], 1)) + "%", ha="center")
    return plot


