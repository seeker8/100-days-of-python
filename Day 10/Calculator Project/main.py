from art import logo
print(logo)

def add(n1, n2):
    """
    Add two numbers
    """
    return n1 + n2

# TODO write out the other 3 functions - subtract, multiply and divide
def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

#  TODO add these 4 functions into a dictionary as the values. Keys =  "+", "-", "*", "/"

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# TODO use the dictionary operations to perform the calculations. Multiply 4 * 8 using the dictionary
# print(operations["*"](4,8))

# TODO calculator
should_user_previous_result = False
should_continue = True
while should_continue:
    first_operand = 0
    if not should_user_previous_result:
        first_operand = float(input("Enter first number: "))
    operator = input("Enter operator +, -, *, /: ")
    second_operand = float(input("Enter second number: "))

    result = operations[operator](first_operand, second_operand)
    print(f"{first_operand} {operator} {second_operand} = {result}")
    continue_running = input("Would you like to continue? (y/n): ")
    if continue_running == "n":
        should_continue = False
        continue
    user_previous_result = input("Would you like to continue working with previous result? (y/n): ")
    if user_previous_result == "y":
        should_user_previous_result = True
        first_operand = result
    else:
        should_user_previous_result = False