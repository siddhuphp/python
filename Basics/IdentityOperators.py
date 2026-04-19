# Identity Operators in Python: 'is' and 'is not'

a = [1, 2, 3]
b = a
c = [1, 2, 3]

# 'is' checks if two variables point to the same object
print(a is b)   # True, because b refers to the same object as a
print(a is c)   # False, because c is a different object with the same contents

# 'is not' checks if two variables do not point to the same object
print(a is not c)  # True, because a and c are different objects

# Example with immutable objects
x = 1000
y = 1000
print(x is y)   # May be False, as integers > 256 are not always cached

# Example with None
z = None
print(z is None)  # True, recommended way to check for None