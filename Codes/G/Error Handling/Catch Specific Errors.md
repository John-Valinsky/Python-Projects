Catch Specific Errors
=====================
try:
    num = int(input("Enter number: "))
    print(100 / num)
except ZeroDivisionError:
    print("Cannot divide by zero")
