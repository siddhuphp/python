#Python Indentation refers to the spaces at the beginning of a code line
if 5 > 2:
 print("Five is greater than two!")

 if 5 > 2:
  print("Five is greater than two!") 
if 5 > 2:
        print("Five is greater than two!")

if 5 > 2:
 print("Five is greater than two!")
 print("Five is greater than two!")

# by default, Python uses 4 spaces for indentation, but you can use any number of spaces as long as it is consistent. However, it is not recommended to use tabs or a mix of tabs and spaces for indentation.
#  if 5 > 2:
#  print("Five is greater than two!")
#         print("Five is greater than two!")


#we can use single quote or double quote for string literals in Python. Both of the following lines of code are valid and will produce the same output:
print("This will work!")
print('This will also work!')

#Print Without a New Line
print("Hello World!", end=" ")
print("I will print on the same line.")

#Mix Text and Numbers
print("I am", 35, "years old.")


#global variables are variables that are defined outside of a function and can be accessed from anywhere in the code. To create a global variable, you simply define it outside of any function. For example:
x = "Hello, World!"  # This is a global variable

def my_function():
    print(x)  # This will access the global variable

my_function()  # This will call the function and print the global variable


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

#Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)



