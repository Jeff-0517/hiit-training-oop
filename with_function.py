" write a program "

def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(a, b):
    if b == 0:
        return
    return a / b

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))


sum_result = add(num1, num2)
product_result = multiply(num1, num2)
division_result = divide(num1, num2)
difference_result = subtract(num1, num2)


print("Addition =", sum_result)
print("Multiplication =", product_result)
print("Division =", division_result)
print("subtraction =", difference_result)