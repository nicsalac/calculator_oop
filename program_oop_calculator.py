from calculator_oop import Calculator
from calculator_for_user_input import UserInput
calc = Calculator(num1, num2)
ui = UserInput

#perform any operations based on user input
if operation == '+':
    print(ui.num1, "+", ui.num2, "=", calc.add())
if operation == '-':
    print(ui.num1, "-", ui.num2, "=", calc.subtract()) 
if operation == '*':
    print(ui.num1, '*', ui.num2, '=', calc.multiply())
if operation == '/':
    print(ui.num1, '/', ui.num2, '=', calc.divide())