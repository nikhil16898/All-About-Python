# set is an unordered collection of unique elements. Sets are mutable, but they do not allow duplicate values. 

# 1> Creating a Set:
# You can create a set by enclosing comma-separated elements within curly braces {}.
my_set = {1, 2, 3, 4, 5}


# 2> Creating a Set from a List:
# You can also create a set by passing a list or any iterable object to the set() function.
my_list = [1, 2, 3, 4, 5]
my_set = set(my_list)


# 3> Adding Elements:
# You can add elements to a set using the add() method.
my_set = {1, 2, 3}
my_set.add(4)


# 4> Removing Elements:
# You can remove elements from a set using the remove() method. If the element does not exist, it raises a KeyError. To avoid this, you can use the discard() method, which does not raise an error if the element is not found.
my_set = {1, 2, 3}
my_set.remove(2)
my_set.discard(4)


# 5> Set Operations:
# Sets support various operations like union (|), intersection (&), difference (-), and symmetric difference (^).
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2
intersection_set = set1 & set2
difference_set = set1 - set2
symmetric_difference_set = set1 ^ set2
  
  
# 6> Set Membership:
# You can test for membership of an element in a set using the in operator.
my_set = {1, 2, 3}
is_present = 2 in my_set

# 7> Set Size:
# You can determine the number of elements in a set using the len() function.
my_set = {1, 2, 3}
size = len(my_set)


# 8> Set Methods:
# Sets provide various built-in methods like pop(), clear(), copy(), and more for manipulation and operations on sets.
my_set = {1, 2, 3}
popped_element = my_set.pop()
my_set.clear()
new_set = my_set.copy()
