# An operator is a symbol or keyword in a programming language that represents a specific operation to be performed on one or more operands.
# For example, in the expression `x + y`, the "+" symbol is the operator, and `x` and `y` are the operands. The operator "+" performs the addition operation on the operands `x` and `y` to produce a result.

# example
x = 2
y = 3
print(x + y)

# 1:. Arithmetic Operators: These operators are used to perform mathematical operations such as addition (+), subtraction (-), multiplication (*), division (/), floor division (//), modulus (%), and exponentiation (**).
x = 5
y = 3

print(x + y)  # Addition: Output: 8
print(x - y)  # Subtraction: Output: 2
print(x * y)  # Multiplication: Output: 15
print(x / y)  # Division: Output: 1.6666666666666667
print(x // y) # Floor Division: Output: 1
print(x % y)  # Modulus: Output: 2
print(x ** y) # Exponentiation: Output: 125

# 2:. Assignment Operators: These operators are used to assign values to variables. Examples include the assignment operator (=), as well as compound assignment operators like +=, -=, *=, /=, //=, %=, and **=.
x = 5
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 8

y = 10
y -= 2  # Equivalent to y = y - 2
print(y)  # Output: 8

# 3:. Comparison Operators: These operators are used to compare the values of two operands. They include == (equal to), != (not equal to), > (greater than), < (less than), >= (greater than or equal to), and <= (less than or equal to).
x = 5
y = 3

print(x == y)  # Equal to: Output: False
print(x != y)  # Not equal to: Output: True
print(x > y)   # Greater than: Output: True
print(x < y)   # Less than: Output: False
print(x >= y)  # Greater than or equal to: Output: True
print(x <= y)  # Less than or equal to: Output: False


# 4:. Logical Operators: These operators are used to combine conditional statements. They include and (logical AND), or (logical OR), and not (logical NOT).
x = True
y = False

print(x and y)  # Logical AND: Output: False
print(x or y)   # Logical OR: Output: True
print(not x)    # Logical NOT: Output: False


# 5:. Bitwise Operators: These operators perform operations on binary representations of integers. They include bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise NOT (~), left shift (<<), and right shift (>>).
x = 5
y = 3

print(x & y)   # Bitwise AND: Output: 1
print(x | y)   # Bitwise OR: Output: 7
print(x ^ y)   # Bitwise XOR: Output: 6
print(~x)      # Bitwise NOT: Output: -6
print(x << y)  # Left Shift: Output: 40
print(x >> y)  # Right Shift: Output: 0


# 6:. Membership Operators: These operators test the membership of a value in a sequence. They include in and not in.
my_list = [1, 2, 3, 4, 5]

print(3 in my_list)     # Output: True
print(6 not in my_list) # Output: True


# 7:. Identity Operators: These operators compare the identity of two objects. They include is and is not.
x = 5
y = 5

print(x is y)      # Output: True
print(x is not y)  # Output: False

# These are the main types of operators in Python. Each type serves a specific purpose and can be used in different contexts to manipulate values and perform operations.