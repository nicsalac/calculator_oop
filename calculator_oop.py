class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


        

# take user input for numbers and operation
num1 = float(input("Enter first number:"))
operation = input("Enter operator [+, -, *, /]:")
num2 = float(input("Enter second number:"))

calc = Calculator(num1, num2)

#perform any operations based on user input
if operation == '+':
    print(num1, "+", num2, "=", calc.add())
if operation == '-':
    print(num1, "-", num2, "=", calc.subtract()) 
if operation == '*':
    print(num1, '*', num2, '=', calc.multiply())
if operation == '/':
    print(num1, '/', num2, '=', calc.divide())