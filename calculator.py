# Simple Calculator

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def calculator():
    print("Simple Calculator")
    
    # Prompt user for two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    # Prompt user for operation
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter choice (1/2/3/4): ")
    
    if operation == '1' or operation == '+':
        result = add(num1, num2)
        print(f"{num1} + {num2} = {result}")
    elif operation == '2' or operation == '-':
        result = subtract(num1, num2)
        print(f"{num1} - {num2} = {result}")
    elif operation == '3' or operation == '*':
        result = multiply(num1, num2)
        print(f"{num1} * {num2} = {result}")
    elif operation == '4' or operation == '/':
        result = divide(num1, num2)
        print(f"{num1} / {num2} = {result}")
    else:
        print("Invalid input. Please select a valid operation.")

# Main program
if __name__ == "__main__":
    calculator()
