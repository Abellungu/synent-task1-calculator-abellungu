print("=== Simple Calculator ===")

try:
    # Get user input
    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    # Perform calculations
    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
            print("Result:", result)
        else:
            print("Error: Cannot divide by zero")

    else:
        print("Invalid operator entered")

except ValueError:
    print("Error: Please enter valid numbers")
