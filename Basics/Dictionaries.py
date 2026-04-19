# Dictionaries in Python - Examples

# 1. Creating a Dictionary
my_dict = {"name": "Alice", "age": 25, "city": "New York"}
print(my_dict)

# 2. Accessing Items
print(my_dict["name"])         # Using key
print(my_dict.get("age"))      # Using get()

# 3. Changing Values
my_dict["age"] = 26
print(my_dict)

# 4. Adding Items
my_dict["email"] = "alice@example.com"
print(my_dict)

# 5. Removing Items
my_dict.pop("city")            # Remove by key
print(my_dict)

del my_dict["email"]           # Remove by key using del
print(my_dict)

my_dict["country"] = "USA"
removed_item = my_dict.popitem()  # Removes last inserted item
print(removed_item)
print(my_dict)

my_dict.clear()                # Remove all items
print(my_dict)

# 6. Looping Through a Dictionary
my_dict = {"name": "Bob", "age": 30, "city": "London"}
for key in my_dict:
    print(key, my_dict[key])

for value in my_dict.values():
    print(value)

for key, value in my_dict.items():
    print(key, value)

# 7. Copying a Dictionary
dict_copy = my_dict.copy()
print(dict_copy)

dict_copy2 = dict(my_dict)
print(dict_copy2)

# 8. Nested Dictionaries
nested_dict = {
    "person1": {"name": "John", "age": 28},
    "person2": {"name": "Jane", "age": 32}
}
print(nested_dict)
print(nested_dict["person1"]["name"])

# 9. List of Dictionary Methods with Examples

sample = {"a": 1, "b": 2}

# keys()
print(sample.keys())

# values()
print(sample.values())

# items()
print(sample.items())

# get()
print(sample.get("a"))

# update()
sample.update({"c": 3})
print(sample)

# pop()
sample.pop("b")
print(sample)

# popitem()
sample.popitem()
print(sample)

# setdefault()
sample.setdefault("d", 4)
print(sample)

# fromkeys()
keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0)
print(new_dict)

# clear()
sample.clear()
print(sample)