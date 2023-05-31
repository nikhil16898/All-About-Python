# tuple is an ordered, immutable collection of elements. Tuples are similar to lists but have some key differences. 

# 1> Creating a Tuple:
# You can create a tuple by enclosing comma-separated elements within parentheses ().
my_tuple = (1, 2, 3, 4, 5)

# 2> Accessing Elements:
# You can access individual elements of a tuple using their index, similar to lists. The index starts from 0 for the first element.my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[0])  # Output: 1
print(my_tuple[2])  # Output: 3


# 3> Immutable Nature:
# Tuples are immutable, meaning their elements cannot be modified after creation. However, you can create new tuples by concatenating or slicing existing tuples.
my_tuple = (1, 2, 3)
new_tuple = my_tuple + (4, 5)
sliced_tuple = my_tuple[1:3]

print(new_tuple)     # Output: (1, 2, 3, 4, 5)
print(sliced_tuple)  # Output: (2, 3)


# 4> Tuple Packing and Unpacking:
# Tuple packing refers to combining multiple values into a single tuple, while tuple unpacking allows you to assign tuple values to individual variables.
my_tuple = 1, 2, 3  # Tuple packing
a, b, c = my_tuple  # Tuple unpacking

print(a, b, c)  # Output: 1 2 3


# 5> Tuple Operations:
# Tuples support various operations such as concatenation (+), repetition (*), and membership (in).
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

concatenated = tuple1 + tuple2
repeated = tuple1 * 3
is_present = 2 in tuple1

print(concatenated)  # Output: (1, 2, 3, 4, 5, 6)
print(repeated)      # Output: (1, 2, 3, 1, 2, 3, 1, 2, 3)
print(is_present)    # Output: True


# 6> Tuple Methods:
# Tuples have limited built-in methods due to their immutability. However, they provide methods like count() and index().
my_tuple = (1, 2, 3, 2, 4, 2)
count_of_2 = my_tuple.count(2)
index_of_4 = my_tuple.index(4)

print(count_of_2)   # Output: 3
print(index_of_4)   # Output: 4
