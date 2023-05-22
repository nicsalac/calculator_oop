class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        

    def add(self):
        return self.num1 + self.num2
        

# take user input for numbers and operation
num1 = float(input("Enter first number:"))
operation = input("Enter operator [+, -, *, /]:")
num2 = float(input("Enter second number:"))

calc = Calculator(num1, num2)

#print the sum of two numbers
if operation == '+':
    print(num1, "+", num2, "=", calc.add())
    