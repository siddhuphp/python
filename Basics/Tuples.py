# Tuples in Python

# 1. Creating Tuples
tuple1 = (1, 2, 3)
tuple2 = ("apple", "banana", "cherry")
tuple3 = (1, "hello", 3.14)
tuple4 = (1,)  # Single element tuple (note the comma)
tuple5 = tuple([4, 5, 6])  # From a list

print("Tuples:")
print(tuple1)
print(tuple2)
print(tuple3)
print(tuple4)
print(tuple5)

# 2. Access Tuples
print("\nAccess Tuples:")
print(tuple2[1])      # banana
print(tuple2[-1])     # cherry
print(tuple1[1:3])    # (2, 3)

# 3. Update Tuples (Tuples are immutable, but you can convert to list and back)
print("\nUpdate Tuples:")
temp_list = list(tuple2)
temp_list[1] = "orange"
tuple2_updated = tuple(temp_list)
print(tuple2_updated)

# 4. Unpack Tuples
print("\nUnpack Tuples:")
a, b, c = tuple1
print(a, b, c)

# Using * to grab remaining elements
tuple6 = (1, 2, 3, 4, 5)
x, y, *z = tuple6
print(x, y, z)

# 5. Loop Tuples
print("\nLoop Tuples:")
for item in tuple3:
    print(item)

# Using index
for i in range(len(tuple3)):
    print(f"Index {i}: {tuple3[i]}")

# 6. Join Tuples
print("\nJoin Tuples:")
tuple7 = tuple1 + tuple2
print(tuple7)

# Repeat tuple
tuple8 = tuple1 * 2
print(tuple8)

# 7. List of all Tuple Methods
print("\nTuple Methods:")
print(dir(tuple))
print("Commonly used methods: count(), index()")

# Example usage:
print("Count of 1 in tuple1:", tuple1.count(1))
print("Index of 'banana' in tuple2:", tuple2.index("banana"))