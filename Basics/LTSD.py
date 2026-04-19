# List Example: Ordered, mutable, allows duplicates
fruits_list = ['apple', 'banana', 'cherry', 'apple']
print("List:", fruits_list)
fruits_list[1] = 'orange'  # Mutable
print("Modified List:", fruits_list)

# Tuple Example: Ordered, immutable, allows duplicates
fruits_tuple = ('apple', 'banana', 'cherry', 'apple')
print("Tuple:", fruits_tuple)
# fruits_tuple[1] = 'orange'  # This will raise an error (immutable)

# Set Example: Unordered, mutable, no duplicates
fruits_set = {'apple', 'banana', 'cherry', 'apple'}
print("Set:", fruits_set)  # 'apple' appears only once
fruits_set.add('orange')   # Mutable
print("Modified Set:", fruits_set)

# Dictionary Example: Key-value pairs, unordered (Python 3.7+ maintains insertion order), mutable, keys must be unique
fruits_dict = {'a': 'apple', 'b': 'banana', 'c': 'cherry'}
print("Dictionary:", fruits_dict)
fruits_dict['b'] = 'orange'  # Mutable
fruits_dict['d'] = 'grape'   # Add new key-value pair
print("Modified Dictionary:", fruits_dict)

# Key Differences:
# List: Ordered, mutable, duplicates allowed
# Tuple: Ordered, immutable, duplicates allowed
# Set: Unordered, mutable, no duplicates
# Dictionary: Unordered (insertion ordered), mutable, key-value pairs, keys unique