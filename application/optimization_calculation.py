import numpy as np
import pandas as pd
from ortools.linear_solver import pywraplp
from matplotlib import pyplot as plt


def optimization_meal(breakfastamr, lunchamr, dinneramr):
    def create_data_model():
        """Stores the data for the problem."""
        data = {}
        data['constraint_coeffs'] = [Cal, TF, SF, Cho, So, Su]
        data['bounds'] = [Cal_max, 100 * meal_ratio, 100 * meal_ratio, 100 * meal_ratio, 100 * meal_ratio,
                          52 * meal_ratio]
        data['obj_coeffs'] = Cal
        data['num_vars'] = len(Cal)
        data['num_constraints'] = len(data['bounds'])
        data['menu_flag'] = menu_flag
        return data

    menu = pd.read_csv("./data/menu.csv")
    # define output
    output = {
        "id": None,
        "name": None,
        "Calories": None,
        "TF": None,
        "SF": None,
        "Cho": None,
        "So": None,
        "Su": None
    }
    # to return none in case status != pywraplp.Solver.OPTIMAL
    breakfast_output = output.copy()
    lunch_output = output.copy()
    dinner_output = output.copy()

    # first constrain coefficients
    # 100% of each nutrients from 2000 kcal
    nutrition_adjust = 2000 / (breakfastamr + lunchamr + dinneramr)
    Cal = menu["Calories"].tolist()
    TF = [x * nutrition_adjust for x in menu["Total Fat (% Daily Value)"].tolist()]
    SF = [x * nutrition_adjust for x in menu["Saturated Fat (% Daily Value)"].tolist()]
    Cho = [x * nutrition_adjust for x in menu["Cholesterol (% Daily Value)"].tolist()]
    So = [x * nutrition_adjust for x in menu["Sodium (% Daily Value)"].tolist()]
    Su = [x * nutrition_adjust for x in menu["Sugars"].tolist()]

    meal = ['Breakfast', 'Lunch', 'Dinner']
    for i_meal in meal:

        if i_meal == 'Breakfast':
            Cal_max = breakfastamr
            meal_ratio = 0.35
            menu_flag = (menu["Category"] == 'Breakfast') | (menu["Category"] == 'Beverages')
            menu_flag = np.multiply(np.array(menu_flag.tolist()), 1)
            menu_flag = menu_flag.tolist()
        elif i_meal == 'Lunch':
            Cal_max = lunchamr
            meal_ratio = 0.35
            menu_flag = (menu["Category"] != 'Breakfast')
            menu_flag = np.multiply(np.array(menu_flag.tolist()), 1)
            menu_flag = menu_flag.tolist()
        else:
            Cal_max = dinneramr
            meal_ratio = 0.30
            menu_flag = (menu["Category"] != 'Breakfast')
            menu_flag = np.multiply(np.array(menu_flag.tolist()), 1)
            menu_flag = menu_flag.tolist()

        data = create_data_model()

        # print(data)
        solver = pywraplp.Solver.CreateSolver('SCIP')
        # define the variable (every x can be any integer)
        infinity = solver.infinity()
        x = {}
        for j in range(data['num_vars']):
            x[j] = solver.IntVar(0, data['menu_flag'][j], 'x[%i]' % j)  # cannot select more than 1 time
        print('Number of variables =', solver.NumVariables())

        # Define the constraints
        for i in range(data['num_constraints']):
            constraint = solver.RowConstraint(0, data['bounds'][i], '')
            for j in range(data['num_vars']):
                constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])
        print('Number of constraints =', solver.NumConstraints())

        # Define the objective
        objective = solver.Objective()
        for j in range(data['num_vars']):
            objective.SetCoefficient(x[j], data['obj_coeffs'][j])
        objective.SetMaximization()

        status = solver.Solve()

        if status == pywraplp.Solver.OPTIMAL:
            calories_selected = solver.Objective().Value()
            print('Objective value =', solver.Objective().Value())
            id_selected = []
            name_selected = []
            X = []
            for j in range(data['num_vars']):
                X.append(x[j].solution_value())
                if x[j].solution_value() > 0:
                    id_selected.append(j)
                    name_selected.append(menu['Item'][j])
                    print(x[j].name(), ' = ', x[j].solution_value(), ' ', menu['Item'][j])
            TF_selected = np.sum(np.multiply(X, TF))
            SF_selected = np.sum(np.multiply(X, SF))
            Cho_selected = np.sum(np.multiply(X, Cho))
            So_selected = np.sum(np.multiply(X, So))
            Su_selected = np.sum(np.multiply(X, Su))

            print('TF: ', TF_selected)
            print('SF: ', SF_selected)
            print('Cho: ', Cho_selected)
            print('So: ', So_selected)
            print('Su: ', Su_selected)

            output['id'] = id_selected
            output['name'] = name_selected
            output['Calories'] = calories_selected
            output['TF'] = TF_selected
            output['SF'] = SF_selected
            output['Cho'] = Cho_selected
            output['So'] = So_selected
            output['Su'] = Su_selected

            if i_meal == 'Breakfast':
                breakfast_output = output.copy()
            elif i_meal == 'Lunch':
                lunch_output = output.copy()
            else:
                dinner_output = output.copy()

            print()
            print('Problem solved in %f milliseconds' % solver.wall_time())
            print('Problem solved in %d iterations' % solver.iterations())
            print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
        else:
            print('The problem does not have an optimal solution.')
    return breakfast_output, lunch_output, dinner_output


