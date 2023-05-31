# dictionary is an unordered collection of key-value pairs. 


# 1> Creating a Dictionary:
# You can create a dictionary by enclosing comma-separated key-value pairs within curly braces {}.
my_dict = {"key1": 'value1', "key2": 'value2', "key3": 'value3'}


# 2> Accessing Values:
# You can access the value associated with a specific key using square brackets [] and the key.
my_dict = {"name": "John", "age": 25, "city": "New York"}
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25



# 3> Modifying Values:
# You can modify the value associated with a key by assigning a new value to it.
my_dict = {"name": "John", "age": 25, "city": "New York"}
my_dict["age"] = 30
print(my_dict["age"])   # Output: 30


# 4> Adding Key-Value Pairs:
# You can add new key-value pairs to a dictionary by assigning a value to a new key.
my_dict = {"name": "John", "age": 25}
my_dict["city"] = "New York"
print(my_dict)   # Output: {"name": "John", "age": 25, "city": "New York"}



# 5>  Removing Key-Value Pairs:
# You can remove a key-value pair from a dictionary using the del keyword followed by the key.
my_dict = {"name": "John", "age": 25, "city": "New York"}
del my_dict["age"]
print(my_dict)   # Output: {"name": "John", "city": "New York"}



# 6> Dictionary Operations:
# Dictionaries support various operations such as checking for key existence using the in keyword, getting the number of key-value pairs using the len() function, and copying dictionaries using the copy() method.
my_dict = {"name": "John", "age": 25, "city": "New York"}
print("age" in my_dict)        # Output: True
print(len(my_dict))            # Output: 3
my_dict_copy = my_dict.copy()



# 7> Dictionary Methods:
# Dictionaries provide built-in methods like keys(), values(), and items() to retrieve the keys, values, and key-value pairs, respectively.
my_dict = {"name": "John", "age": 25, "city": "New York"}
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()


