# Show usage of different basic datatypes in Python

# String
my_string = "Hello, world!"
print(my_string)

# List
my_list = [5, 10, 15, 20, 25]
for i in my_list:
    print(i)

# Tuples
my_tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
for i in my_tup:
    print(i)

# Dict
my_dict = {"name": "Laurent", "age": 26, "occupation": "Data Analyst"}
for key, val in my_dict.items():
    print("My {} is {}".format(key, val))

# Set
my_set = {10, 20, 10, 30, 50, 20, 40, 30}
for i in my_set:
    print(i)
