# Examples of Sets in Python

# Creating a set
my_set = {1, 2, 3, 4}
print("Set:", my_set)

# Accessing elements (sets are unordered, so no indexing)
for item in my_set:
    print("Accessed item:", item)

# Adding elements
my_set.add(5)
print("After add:", my_set)

# Adding multiple elements
my_set.update([6, 7])
print("After update:", my_set)

# Removing elements
my_set.remove(3)  # Raises KeyError if not present
print("After remove:", my_set)

# Discarding elements (no error if not present)
my_set.discard(10)
print("After discard:", my_set)

# Popping an element (removes and returns an arbitrary element)
popped = my_set.pop()
print("Popped element:", popped)
print("After pop:", my_set)

# Looping through a set
for val in my_set:
    print("Looped value:", val)

# Joining sets (union)
set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union:", union_set)

# Intersection
intersection_set = set1.intersection(set2)
print("Intersection:", intersection_set)

# Difference
diff_set = set1.difference(set2)
print("Difference:", diff_set)

# Symmetric Difference
sym_diff_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", sym_diff_set)

# Frozenset (immutable set)
frozen = frozenset([1, 2, 3])
print("Frozenset:", frozen)

# List of common set methods
methods = [
    "add", "clear", "copy", "difference", "difference_update",
    "discard", "intersection", "intersection_update", "isdisjoint",
    "issubset", "issuperset", "pop", "remove", "symmetric_difference",
    "symmetric_difference_update", "union", "update"
]
print("Set methods:", methods)