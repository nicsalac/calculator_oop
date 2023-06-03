from calculator_oop import Calculator
from calculator_oop import NewCalculator
from calculator_for_user_input import UserInput



ui = UserInput()
num1, num2, operation = ui.get_user_input()
calc = Calculator(num1, num2)
newcalc = NewCalculator(num1, num2)

#perform any operations based on user input
if operation == '+':
    print(num1, "+", num2, "=", calc.add())
elif operation == '-':
    print(num1, "-", num2, "=", calc.subtract()) 
elif operation == '*':
    print(num1, '*', num2, '=', calc.multiply())
elif operation == '/':
    print(num1, '/', num2, '=', calc.divide())
elif operation == 'square' :
    print("square of" ,num1, "is", newcalc.square, "and the square of", num2, "is", newcalc.square())
elif operation == 'cube':
    print("cube of" ,num1, "is", newcalc.cube, "and the cube of", num2, "is", newcalc.cube())
else:
    print("Invalid operator entered.")