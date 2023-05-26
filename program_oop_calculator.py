from calculator_oop import Calculator
from calculator_for_user_input import UserInput

ui = UserInput()
num1, num2, operation = ui.get_user_input()
calc = Calculator(num1, num2)

#perform any operations based on user input
if operation == '+':
    print(num1, "+", num2, "=", calc.add())
elif operation == '-':
    print(num1, "-", num2, "=", calc.subtract()) 
elif operation == '*':
    print(num1, '*', num2, '=', calc.multiply())
elif operation == '/':
    print(num1, '/', num2, '=', calc.divide())
else:
    print("Invalid operator entered.")