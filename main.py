import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def divide(n1, n2):
    if n2 == 0:
        return "Error! Division by zero."
    return n1 / n2

def multiply(n1, n2):
    return n1 * n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

print(art.logo)

def calculator():
    previous_result = None

    while True:
        if previous_result is None:
            num1 = float(input("What's the first number?: "))
        else:
            num1 = previous_result

        print("+\n-\n*\n/")

        operator = input("Pick an operation: ")

        if operator not in operations:
            print("Invalid operator! Try again.")
            continue

        num2 = float(input("What's the next number?: "))

        result = operations[operator](num1, num2)
        print(f"{num1} {operator} {num2} = {result}")

        choice = input("Type 'y' to continue calculating with 5.0, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            previous_result = result
        else:
            previous_result = None
            print("\n" * 50)

calculator()