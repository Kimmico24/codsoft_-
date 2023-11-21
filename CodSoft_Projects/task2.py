# Function to perform addition
def add(x, y):
    return x + y


# Function to perform subtraction
def subtract(x, y):
    return x - y


# Function to perform multiplication
def multiply(x, y):
    return x * y


# Function to perform division
def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y


# Input from the user
while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # Display the operation options
        print("Available operations:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")

        choice = input("Enter your choice (1/2/3/4): ")

        # Perform the calculation based on the user's choice
        if choice == '1':
            result = add(num1, num2)
        elif choice == '2':
            result = subtract(num1, num2)
        elif choice == '3':
            result = multiply(num1, num2)
        elif choice == '4':
            result = divide(num1, num2)
        else:
            print("Invalid choice")
            continue

        print("Result: ", result)

        # Ask the user if they want to perform another calculation
        another_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if another_calculation.lower() != "yes":
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
