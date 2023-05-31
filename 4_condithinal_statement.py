# Conditional statements in Python allow you to control the flow of your program based on certain conditions. They help you make decisions and execute different blocks of code depending on whether a condition is true or false.

# 1> if statement:.
# The if statement is used to execute a block of code if a certain condition is true.
x = 5

if x > 0:
    print("x is positive")


# 2> if-else statement:
# The if-else statement allows you to execute one block of code if a condition is true and another block of code if the condition is false.
x = 5

if x > 0:
    print("x is positive")
else:
    print("x is not positive")


# 3> if-elif-else statement:
# The if-elif-else statement is used when there are multiple conditions to be checked. It allows you to specify multiple conditions and execute different blocks of code based on the first condition that evaluates to true.
x = 5

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")


# 4> Nested if statements:
# You can also have nested if statements, where one if statement is nested inside another if or else block.
x = 5

if x > 0:
    print("x is positive")
    if x % 2 == 0:
        print("x is even")
    else:
        print("x is odd")


# These are the basic conditional statements in Python.