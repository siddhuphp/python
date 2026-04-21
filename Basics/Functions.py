import functools

def test_function():
    print("test function call")

test_function()

#another example

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# Python Decorators Examples

# Simple decorator
def my_decorator(func):
  def wrapper():
    print("Before function call")
    func()
    print("After function call")
  return wrapper

@my_decorator
def say_hello():
  print("Hello!")

say_hello()

# Decorator with arguments
def repeat(times):
  def decorator(func):
    def wrapper(*args, **kwargs):
      for _ in range(times):
        func(*args, **kwargs)
    return wrapper
  return decorator

@repeat(3)
def greet(name):
  print(f"Hello, {name}!")

greet("Alice")

# Decorator preserving function metadata

def log_function(func):
  @functools.wraps(func)
  def wrapper(*args, **kwargs):
    print(f"Calling {func.__name__}")
    result = func(*args, **kwargs)
    print(f"{func.__name__} returned {result}")
    return result
  return wrapper

@log_function
def add(a, b):
  return a + b

result = add(5, 3)

# Python Lambda Examples

# Simple lambda function
square = lambda x: x ** 2
print(square(5))  # Output: 25

# Lambda with multiple arguments
add_numbers = lambda a, b: a + b
print(add_numbers(10, 20))  # Output: 30

# Lambda with map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]

# Lambda with filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8, 10]