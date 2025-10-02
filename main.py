# Simple Calculator in Python
# Initialize repeat variable
rep = str("y")

# Take user input
# Perform calculation based on the operator
while rep == 'y':
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: Division by zero!"
    else:
        result = "Error: Invalid operator!"

    # Display result
    print("Result:", result)

    # Ask if the user wants to perform another calculation
    rep = input("Do you want to perform another calculation? (y/n): ")
    while rep != 'y' and rep != 'n':
        print("please enter y or n")
        rep = input("Do you want to perform another calculation? (y/n): ")
    
