# Python 3.10+ required for match-case statements

# 1. Simple value matching
def simple_match(x):
    match x:
        case 1:
            return "One"
        case 2:
            return "Two"
        case _:
            return "Other"

# 2. Matching with multiple values
def multi_value_match(x):
    match x:
        case 1 | 2 | 3:
            return "One, Two, or Three"
        case _:
            return "Other"

# 3. Matching types
def type_match(x):
    match x:
        case int():
            return "Integer"
        case str():
            return "String"
        case list():
            return "List"
        case _:
            return "Other type"

# 4. Matching sequences (list unpacking)
def sequence_match(seq):
    match seq:
        case [a, b]:
            return f"Two elements: {a}, {b}"
        case [a, b, c]:
            return f"Three elements: {a}, {b}, {c}"
        case [a, *rest]:
            return f"First: {a}, Rest: {rest}"
        case _:
            return "Other sequence"

# 5. Matching dictionaries
def dict_match(d):
    match d:
        case {"type": "point", "x": x, "y": y}:
            return f"Point at ({x}, {y})"
        case {"type": "circle", "radius": r}:
            return f"Circle with radius {r}"
        case _:
            return "Unknown shape"

# 6. Matching with guards (if conditions)
def guard_match(x):
    match x:
        case int() as n if n > 0:
            return "Positive integer"
        case int() as n if n < 0:
            return "Negative integer"
        case _:
            return "Other"

# 7. Matching custom classes
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def class_match(obj):
    match obj:
        case Point(x=0, y=0):
            return "Origin"
        case Point(x, y):
            return f"Point at ({x}, {y})"
        case _:
            return "Not a Point"

# 8. Nested patterns
def nested_match(data):
    match data:
        case {"user": {"name": name, "age": age}}:
            return f"User {name}, age {age}"
        case _:
            return "No user info"

# Example usage
if __name__ == "__main__":
    print(simple_match(2))
    print(multi_value_match(3))
    print(type_match([1, 2]))
    print(sequence_match([1, 2, 3]))
    print(dict_match({"type": "point", "x": 1, "y": 2}))
    print(guard_match(-5))
    print(class_match(Point(0, 0)))
    print(nested_match({"user": {"name": "Alice", "age": 30}}))