def calculator(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Modulo by zero is not allowed"
        return num1 % num2
    else:
        return "Invalid operator"


# User input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

result = calculator(num1, num2, operator)
print("Result:", result)
