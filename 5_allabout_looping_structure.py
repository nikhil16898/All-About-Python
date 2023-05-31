# Looping structures in Python allow you to repeatedly execute a block of code until a certain condition is met or for a specific number of iterations. Python provides several looping structures, including:

# 1> while loop:
# The while loop executes a block of code as long as a specified condition is true.
x = 0

while x < 5:
    print(x)
    x += 1


# 2> for loop:
# The for loop is used to iterate over a sequence (such as a list, tuple, or string) or other iterable objects.
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)


# 3> range() function:
# The range() function is often used in conjunction with the for loop to generate a sequence of numbers.
for i in range(5):
    print(i)


# 4> Nested loops:
# You can have loops within loops, creating nested structures for more complex iterations.
for i in range(3):
    for j in range(2):
        print(i, j)

# 5> break statement:
# The break statement is used to exit a loop prematurely, regardless of the loop condition.
x = 0

while True:
    print(x)
    x += 1
    if x == 5:
        break

# 6> continue statement:
# The continue statement is used to skip the current iteration and move to the next iteration of the loop.
for i in range(5):
    if i == 2:
        continue
    print(i)
