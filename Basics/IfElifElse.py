# Example 1: Basic if, elif, else
x = 10

if x > 15:
    print("x is greater than 15")
elif x > 5:
    print("x is greater than 5 but less than or equal to 15")
else:
    print("x is 5 or less")

# Example 2: Checking user input
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

# Example 3: Grading system
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

    # Example 4: Nested if else
    number = 7

    if number > 0:
        print("Number is positive")
        if number % 2 == 0:
            print("Number is even")
        else:
            print("Number is odd")
    else:
        print("Number is zero or negative")