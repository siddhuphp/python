class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
# Create an instance of class A
person1 = A("Alice", 30)
person1.display()  # Output: Name: Alice, Age: 30

# Inheritance Example
class B(A):
    def __init__(self, name, age, city):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.city = city

    def display(self):
        super().display()  # Call the display method of the parent class
        print("City:", self.city)

# Create an instance of class B
person2 = B("Bob", 25, "New York")
person2.display()  # Output: Name: Bob, Age: 25, City: New York

# Polymorphism Example
class C(A):
    def display(self):
        print("This is class C")
        super().display()  # Call the display method of the parent class

person3 = C("Charlie", 35)
person3.display()  # Output: This is class C, Name: Charlie, Age: 35

# Encapsulation Example
class D:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def get_name(self):
        return self.__name  # Getter method

    def set_name(self, name):
        self.__name = name  # Setter method
person4 = D("David")
print("Name:", person4.get_name())  # Output: Name: David
person4.set_name("Eve")
print("Updated Name:", person4.get_name())  # Output: Updated Name: Eve

#Clear examples of public, private, and protected members in Python
class E:
    def __init__(self):
        self.public_var = "I am public"  # Public member
        self._protected_var = "I am protected"  # Protected member (convention)
        self.__private_var = "I am private"  # Private member

    def get_private_var(self):
        return self.__private_var  # Accessing private member through a method 
e = E()
print(e.public_var)  # Output: I am public
print(e._protected_var)  # Output: I am protected (can be accessed but should be treated as protected)
# print(e.__private_var)  # This will raise an error (private member)
print(e.get_private_var())  # Output: I am private

# Example of method overriding
class F(A):
    def display(self):
        print("This is class F")
        super().display()  # Call the display method of the parent class   
person5 = F("Frank", 40)
person5.display()  # Output: This is class F, Name: Frank, Age: 40


# Example of method overloading (using default arguments)
class G:    
    def display(self, name=None):
        if name:
            print("Hello, " + name)
        else:
            print("Hello, World!")
g = G()
g.display()  # Output: Hello, World!
g.display("Grace")  # Output: Hello, Grace


# Example of multiple inheritance
class H:
    def method_h(self):
        print("Method from class H")
class I:
    def method_i(self):
        print("Method from class I")
class J(H, I):
    def method_j(self):
        print("Method from class J")
j = J()
j.method_h()  # Output: Method from class H
j.method_i()  # Output: Method from class I
j.method_j()  # Output: Method from class J


# Example of using super() to call parent class methods
class K(A):
    def __init__(self, name, age, profession):
        super().__init__(name, age)  # Call the constructor of the parent class
        self.profession = profession

    def display(self):
        super().display()  # Call the display method of the parent class
        print("Profession:", self.profession)
person6 = K("Karen", 28, "Engineer")
person6.display()  # Output: Name: Karen, Age: 28, Profession: Engineer

# Example of using class methods and static methods
class L:
    class_variable = "I am a class variable"

    @classmethod
    def class_method(cls):
        print("This is a class method. Class variable:", cls.class_variable)

    @staticmethod
    def static_method():
        print("This is a static method. It does not access class or instance variables.")
L.class_method()  # Output: This is a class method. Class variable: I am a class variable
L.static_method()  # Output: This is a static method. It does not access class or instance variables.

# Example of using properties for encapsulation
class M:
    def __init__(self, name):
        self._name = name  # Protected attribute

    @property
    def name(self):
        return self._name  # Getter method

    @name.setter
    def name(self, value):
        self._name = value  # Setter method
m = M("Mike")
print("Name:", m.name)  # Output: Name: Mike
m.name = "John"
print("Updated Name:", m.name)  # Output: Updated Name: John

# Examples of multiple classes and objects with different attributes and methods with public, private, and protected members
class N:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello, " + self.name)
class O:
    def __init__(self, name):
        self._name = name  # Protected attribute

    def greet(self):
        print("Hi, " + self._name)
class P:
    def __init__(self, name):
        self.__name = name  # Private attribute

    def greet(self):
        print("Hey, " + self.__name)
n = N("Nina")
o = O("Oscar")
p = P("Paul")
n.greet()  # Output: Hello, Nina
o.greet()  # Output: Hi, Oscar
p.greet()  # Output: Hey, Paul

# Example of using __str__ method for string representation of objects
class Q:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Q(name={self.name}, age={self.age})"
q = Q("Quincy", 22)
print(q)  # Output: Q(name=Quincy, age=22)


# Example of using __repr__ method for official string representation of objects
class R:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"R(name={self.name}, age={self.age})"
r = R("Rachel", 30)
print(repr(r))  # Output: R(name=Rachel, age=30)

# Example of using __eq__ method for object comparison
class S:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        if isinstance(other, S):
            return self.name == other.name and self.age == other.age
        return False
s1 = S("Sam", 25)
s2 = S("Sam", 25)
s3 = S("Sara", 28)
print(s1 == s2)  # Output: True (s1 and s2 are considered equal)
print(s1 == s3)  # Output: False (s1 and s3 are not equal)

# Example of using __len__ method for getting the length of an object
class T:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)
t = T([1, 2, 3, 4, 5])
print(len(t))  # Output: 5

# Examples of Inner Classes
class U:
    class Inner:
        def inner_method(self):
            print("This is an inner class method.")
u = U()
inner_instance = u.Inner()
inner_instance.inner_method()  # Output: This is an inner class method.

# example of Accessing Inner Class from the Outside
class Outer:
  def __init__(self):
    self.name = "Outer"

  class Inner:
    def __init__(self):
      self.name = "Inner"

    def display(self):
      print("Hello from inner class")

outer = Outer()
inner = outer.Inner()
inner.display()

