class Equation:
    def __init__(self):
        self.clauses = []
        self.variables = []
        self.variable_values = []

clauses = []
variables = []
variable_values = []

myFile = open("equation.txt", "r")
print(myFile.read())
myFile.close()

with open('equation.txt', 'r') as myFile:
    equation = myFile.read()

for x in equation:
    if x is not ' ' and x is not '(' and x is not ')' and x is not '!' and x is not '*' and x is not '+':
        if not variables.__contains__(x):
            variables.append(x)

variables.sort()
for x in variables:
    value = input("Input value for " + x + ":   ")
    variable_values.append((x, value))

clauses = equation.split("*")

for x in variable_values:
    equation = equation.replace(x[0], x[1])
equation = equation.replace("!", str("not "))
equation = equation.replace("+", str("or"))
equation = equation.replace("*", str("and"))
print("\n")
print(equation + "\n")
evaluation = eval(equation)
print("Evaluation:   " + str(evaluation))
pause = input("\n\nPress Enter to continue.")
x = 0
