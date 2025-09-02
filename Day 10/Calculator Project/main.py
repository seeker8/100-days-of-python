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
print(operations["*"](4,8))