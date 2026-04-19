# Membership Operators Examples in Python

# 'in' operator
fruits = ['apple', 'banana', 'cherry']
print('banana' in fruits)      # True
print('orange' in fruits)      # False

# 'not in' operator
numbers = [1, 2, 3, 4, 5]
print(3 not in numbers)        # False
print(10 not in numbers)       # True

# With strings
sentence = "Hello, world!"
print('world' in sentence)     # True
print('Python' not in sentence) # True

# With dictionaries (checks keys)
person = {'name': 'Alice', 'age': 25}
print('name' in person)        # True
print('Alice' in person)       # False