# functions are blocks of reusable code that perform specific tasks. 

# 1> Function Definition:
# To define a function in Python, you use the def keyword followed by the function name, parentheses for optional parameters, and a colon. The function body is indented below the definition.
def greet():
    print("Hello, world!")


# 2> Function Parameters:
# Functions can take input parameters, which are specified within the parentheses in the function definition. These parameters act as placeholders for values that are passed when the function is called.
def greet(name):
    print("Hello, " + name + "!")


# 3> Return Statement:
# Functions can return values using the return statement. This allows you to obtain results or pass data back to the caller.
def add(x, y):
    return x + y


# 4> Function Invocation:
# To execute a function, you call or invoke it by using its name followed by parentheses. Arguments can be passed inside the parentheses if the function expects parameters.
greet("Alice")  # Output: Hello, Alice!
result = add(3, 5)  # result = 8


# 5> Default Parameters:
# You can define default values for function parameters, making them optional. If an argument is not provided, the default value is used.
def greet(name="world"):
    print("Hello, " + name + "!")


# 6> Variable Number of Arguments:
# Python functions can handle a variable number of arguments using *args (for non-keyword arguments) and **kwargs (for keyword arguments). This allows for flexibility in function calls.
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    return total


# 7> Recursive Functions:
# A recursive function is one that calls itself within its own body. It allows for solving problems by breaking them down into smaller, similar sub-problems.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

