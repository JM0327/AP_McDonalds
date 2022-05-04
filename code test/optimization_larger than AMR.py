import pandas as pd
from ortools.linear_solver import pywraplp

menu = pd.read_csv("./menu.csv")
# print(menu.head())

# first constrain coefficients
Cal = menu["Calories"].tolist()
TF = menu["Total Fat (% Daily Value)"].tolist()
SF = menu["Saturated Fat (% Daily Value)"].tolist()
Cho = menu["Cholesterol (% Daily Value)"].tolist()
So = menu["Sodium (% Daily Value)"].tolist()
Su = menu["Sugars"].tolist()


def create_data_model():
    """Stores the data for the problem."""
    data = {}
    data['constraint_coeffs'] = [Cal, TF, SF, Cho, So, Su]
    data['bounds'] = [2102, 100, 100, 100, 100, 52]
    data['obj_coeffs'] = Cal
    data['num_vars'] = len(Cal)
    data['num_constraints'] = 6
    return data

data = create_data_model()
# print(data)

solver = pywraplp.Solver.CreateSolver('SCIP')

# define the variable (every x can be any integer)
infinity = solver.infinity()
x = {}
for j in range(data['num_vars']):
    x[j] = solver.IntVar(0, 3, 'x[%i]' % j)
print('Number of variables =', solver.NumVariables())

# Define the constraints(the first constraint is larger than and other constraints are smaller than)
for i in range(data['num_constraints']):
    if i == 0:
        constraint = solver.RowConstraint(data['bounds'][i], infinity, '')
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])
    else:
        constraint = solver.RowConstraint(0, data['bounds'][i], '')
        for j in range(data['num_vars']):
            constraint.SetCoefficient(x[j], data['constraint_coeffs'][i][j])

print('Number of constraints =', solver.NumConstraints())

# Define the objective
objective = solver.Objective()
for j in range(data['num_vars']):
    objective.SetCoefficient(x[j], data['obj_coeffs'][j])
objective.SetMinimization()

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