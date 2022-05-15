import numpy as np
import pandas as pd
from ortools.linear_solver import pywraplp

menu = pd.read_csv("./menu.csv")

# first constrain coefficients
Cal0 = menu["Calories"].tolist()
#Cal=[]
#for cal in Cal0:
#    cal = (-1) * cal
#    Cal.append(cal)
Cal = [i * -1 for i in Cal0]
TF = menu["Total Fat (% Daily Value)"].tolist()
SF = menu["Saturated Fat (% Daily Value)"].tolist()
Cho = menu["Cholesterol (% Daily Value)"].tolist()
So = menu["Sodium (% Daily Value)"].tolist()
Su = menu["Sugars"].tolist()

def main():
    def create_data_model():
        """Stores the data for the problem."""
        data = {}
        data['constraint_coeffs'] = [Cal0, TF, SF, Cho, So, Su]
        data['bounds'] = [Cal_max, 100, 100, 100, 100, 51.67]
        data['obj_coeffs'] = Cal0
        data['num_vars'] = len(Cal)
        data['num_constraints'] = len(data['bounds'])
        data['menu_flag'] = menu_flag
        return data

    meal = ['Breakfast', 'Lunch', 'Dinner']
    for i_meal in meal:
        if i_meal == 'Breakfast':
            Cal_max = 600  # change to be AMR per meal
            menu_flag = (menu["Category"] == 'Breakfast') | (menu["Category"] == 'Beverages')
            menu_flag = np.multiply(np.array(menu_flag.tolist()),1)
            menu_flag = menu_flag.tolist()
        elif i_meal == 'Lunch':
            Cal_max = 750
            menu_flag = (menu["Category"] != 'Breakfast')
            menu_flag = np.multiply(np.array(menu_flag.tolist()), 1)
            menu_flag = menu_flag.tolist()
        else:
            Cal_max = 600
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
            x[j] = solver.IntVar(0, data['menu_flag'][j], 'x[%i]' % j) #cannot select more than 1 time, we can change inf to be 1
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
            print('Objective value =', solver.Objective().Value())
            for j in range(data['num_vars']):
                if x[j].solution_value() > 0:
                    print(x[j].name(), ' = ', x[j].solution_value(), ' ', menu['Item'][j])
            print()
            print('Problem solved in %f milliseconds' % solver.wall_time())
            print('Problem solved in %d iterations' % solver.iterations())
            print('Problem solved in %d branch-and-bound nodes' % solver.nodes())
        else:
            print('The problem does not have an optimal solution.')

if __name__ == '__main__':
    main()


