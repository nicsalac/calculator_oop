class UserInput:
   def get_user_input(self):
        num1 = float(input("Enter first number: "))
        operation = input("Enter operation (+,-,*,/): ")
        num2 = float(input("Enter second number: "))
        return num1, num2, operation

