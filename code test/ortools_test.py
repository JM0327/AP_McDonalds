import pandas as pd
import numpy
from ortools.linear_solver import pywraplp


def main():
    # read menu file
    data = pd.read_csv('../data/menu.csv')
    menu = data.values.tolist()

    # Nutrient minimums.
    nutrients = [
        ['Calories (kcal)', 3],
        ['Protein (g)', 70],
        ['Calcium (g)', 0.8],
        ['Iron (mg)', 12],
        ['Vitamin A (KIU)', 5],
        ['Vitamin B1 (mg)', 1.8],
        ['Vitamin B2 (mg)', 2.7],
        ['Niacin (mg)', 18],
        ['Vitamin C (mg)', 75],
    ]

    # Declare an array to hold our variables.
    solver = pywraplp.Solver('Example',
                             pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

    # Declare an array to hold our variables.
    foods = [solver.NumVar(0.0, solver.infinity(), item[0]) for item in menu]
    print('Number of variables =', solver.NumVariables())

    # Create the constraints, one per nutrient.
    constraints = []
    for i, nutrient in enumerate(nutrients):
        constraints.append(solver.Constraint(nutrient[1], solver.infinity()))
        for j, item in enumerate(menu):
            constraints[i].SetCoefficient(foods[j], item[i + 3])
    print('Number of constraints =', solver.NumConstraints())

    # Objective function: Minimize the sum of (price-normalized) foods.
    objective = solver.Objective()
    for food in foods:
        objective.SetCoefficient(food, 1)
    objective.SetMinimization()

    status = solver.Solve()

    # Check that the problem has an optimal solution.
    if status != solver.OPTIMAL:
        print('The problem does not have an optimal solution!')
        if status == solver.FEASIBLE:
            print('A potentially suboptimal solution was found.')
        else:
            print('The solver could not solve the problem.')
            exit(1)
    # Display the amounts (in dollars) to purchase of each food.
    nutrients_result = [0] * len(nutrients)
    print('\nAnnual Foods:')
    for i, food in enumerate(foods):
        if food.solution_value() > 0.0:
            print('{}: ${}'.format(menu[i][0], 365. * food.solution_value()))
            for j, _ in enumerate(nutrients):
                nutrients_result[j] += menu[i][j + 3] * food.solution_value()
    print('\nOptimal annual price: ${:.4f}'.format(365. * objective.Value()))

    print('\nNutrients per day:')
    for i, nutrient in enumerate(nutrients):
        print('{}: {:.2f} (min {})'.format(nutrients[0], nutrients_result[i],
                                           nutrients[1]))


if __name__ == '__main__':
    main()
