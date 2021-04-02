# converts a given object n to either an int, or a float
# will return n if unable to
def num(n):
    try:
        return int(n)
    except ValueError:
        try:
            return float(n)
        except ValueError:
            return n

# given a variable n, check if it is a number
# returns True if so, False otherwise
def is_num(n):
    n = num(n)
    return type(n) == int or type(n) == float

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

# This function divides two numbers
def divide(x, y):
    return x / y 

# This function returns the modulus of two numbers
def mod(x, y):
    return x % y

# This function returns the exponent x^y
def exp(x, y):
    return x ** y