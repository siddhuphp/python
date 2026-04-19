# List Examples in Python

# 1. Creating Lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]

# 2. Accessing and Changing List Items
print(fruits[1])           # Output: banana
fruits[1] = "blueberry"    # Change item
print(fruits)              # Output: ['apple', 'blueberry', 'cherry']

# 3. Adding List Items
fruits.append("orange")    # Add at end
fruits.insert(1, "kiwi")   # Insert at position 1
print(fruits)              # Output: ['apple', 'kiwi', 'blueberry', 'cherry', 'orange']

# 4. Removing List Items
fruits.remove("kiwi")      # Remove by value
fruits.pop()               # Remove last item
del fruits[0]              # Remove by index
print(fruits)              # Output: ['blueberry', 'cherry']

# 5. Looping Through a List
for fruit in fruits:
    print(fruit)

# 6. List Comprehension
squares = [x**2 for x in numbers]
print(squares)             # Output: [1, 4, 9, 16, 25]

# 7. Sorting Lists
numbers.sort()             # Ascending
numbers.sort(reverse=True) # Descending
fruits.sort()              # Alphabetical
print(numbers)
print(fruits)

# 8. Copying Lists
copy1 = fruits.copy()
copy2 = list(fruits)
print(copy1, copy2)

# 9. List Methods
fruits.append("apple")
print(fruits.count("apple"))   # Count occurrences
fruits.extend(["pear", "grape"]) # Add multiple items
print(fruits.index("cherry"))  # Find index
fruits.reverse()               # Reverse order
fruits.clear()                 # Remove all items
print(fruits)

# 10. Exercises
# a. Create a list of 5 numbers and print only even numbers
nums = [10, 15, 20, 25, 30]
for n in nums:
    if n % 2 == 0:
        print(n)

# b. Use list comprehension to create a list of squares from 1 to 10
squares = [i*i for i in range(1, 11)]
print(squares)

# c. Remove all occurrences of a specific value from a list
vals = [1, 2, 3, 2, 4, 2]
vals = [v for v in vals if v != 2]
print(vals)


# Example: Demonstrating various list methods
sample = [3, 1, 4, 1, 5, 9, 2]

# append()
sample.append(6)
print("append:", sample)

# extend()
sample.extend([5, 3])
print("extend:", sample)

# insert()
sample.insert(2, 7)
print("insert:", sample)

# remove()
sample.remove(1)  # removes first occurrence of 1
print("remove:", sample)

# pop()
popped = sample.pop()
print("pop:", popped, sample)

# clear()
copy_sample = sample.copy()
copy_sample.clear()
print("clear:", copy_sample)

# index()
idx = sample.index(4)
print("index of 4:", idx)

# count()
cnt = sample.count(5)
print("count of 5:", cnt)

# sort()
sample.sort()
print("sort:", sample)

# reverse()
sample.reverse()
print("reverse:", sample)

# copy()
copied = sample.copy()
print("copy:", copied)