# This file shows how to use list comprehensions to cleanly create a list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# creates a list of the squares of each number in my_list
squares = [num * num for num in my_list]
print(squares)
