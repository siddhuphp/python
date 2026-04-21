# Examples of while loops

# 1. Basic while loop
count = 0
while count < 5:
    print("Count is:", count)
    count += 1

# 2. While loop with else
n = 3
while n > 0:
    print(n)
    n -= 1
else:
    print("Loop ended")

# 3. Infinite while loop (with break)
i = 0
while True:
    print("Infinite loop, i =", i)
    i += 1
    if i == 3:
        break

# 4. While loop with continue
x = 0
while x < 5:
    x += 1
    if x == 3:
        continue
    print("x is", x)

# Examples of for loops

# 1. For loop over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. For loop with range
for i in range(3):
    print("i =", i)

# 3. For loop with else
for i in range(2):
    print("Looping", i)
else:
    print("For loop ended")

# 4. For loop with break
for i in range(5):
    if i == 2:
        break
    print("Breaking at", i)

# 5. For loop with continue
for i in range(5):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# 6. For loop over dictionary
person = {"name": "Alice", "age": 25}
for key, value in person.items():
    print(key, ":", value)