# Examples of control flow using Python

# Prints numbers 1 to 10 using a for loop
for i in range(1, 11):
    print(i)

# Prints numbers 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i += 1

# Compares the value of a and b using an if/elif/else statement
a = 10
b = 20
if a < b:
    print("{} is less than {}".format(a, b))
elif a == b:
    print("{} is equal to {}".format(a, b))
else:
    print("{} is greater than {}".format(a, b))
