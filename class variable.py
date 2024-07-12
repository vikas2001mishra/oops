#Example 1. Here's an example to illustrate class variables:

'''
class MyClass:
    class_variable = 10  # This is a class variable

    def __init__(self, instance_variable):
        self.instance_variable = instance_variable  # This is an instance variable

# Create instances of MyClass
obj1 = MyClass(20)
obj2 = MyClass(30)

# Accessing class variable through class name
print(MyClass.class_variable)  # Output: 10

# Accessing class variable through instance
print(obj1.class_variable)  # Output: 10

# Modifying class variable
MyClass.class_variable = 100

# The change is reflected in all instances
print(obj1.class_variable)  # Output: 100
print(obj2.class_variable)  # Output: 100

'''

#Example 2.

'''
class Test:
    x = 10  # Class variable

    def __init__(self):
        self.y = 20  # Instance variable

# Create two instances of the Test class
t1 = Test()
t2 = Test()

# Print the initial values of t1 and t2
print(t1.x, t1.y)  # Expected output: 10 20
print(t2.x, t2.y)  # Expected output: 10 20

# Modify t1's class variable and t2's instance variable
t1.x = 888
t2.y = 1000

# Print the values after modification
print(t1.x, t1.y)  # Expected output: 888 20
print(t2.x, t2.y)  # Expected output: 10 1000
'''

#Example 3.

'''
class Test:
    a = 10  # Class variable

    def __init__(self):  # Correct constructor method
        self.b = 20  # Instance variable

    def m1(self):
        self.a = 888  # Creates an instance variable 'a' for t1
        self.b = 999  # Modifies the instance variable 'b'

# Create two instances of the Test class
t1 = Test()
t2 = Test()

# Call method m1 on t1 to modify its variables
t1.m1()

# Print the values of instance and class variables for t1
print(t1.a, t1.b)  # Expected output: 888 999

# Print the values of instance and class variables for t2
print(t2.a, t2.b)  # Expected output: 10 20 (t2 remains unaffected by t1's method call)
'''

#Example 4.

'''
class Test:
    a = 10  # Class variable

    def __init__(self):
        self.b = 20  # Instance variable

    @classmethod
    def m1(cls):
        cls.a = 888  # Modify class variable 'a'
        # cls.b = 999  # This will cause an error because 'b' is not a class variable

# Create two instances of the Test class
t1 = Test()
t2 = Test()

# Call the class method m1 on t1
t1.m1()

# Print the values of instance and class variables for t1
print(t1.a, t1.b)  # Expected output: 888 20

# Print the values of instance and class variables for t2
print(t2.a, t2.b)  # Expected output: 888 20 (class variable 'a' is shared)

# Print the values of the class variable directly from the class
print(Test.a)      # Expected output: 888

# Trying to print Test.b will raise an AttributeError because 'b' is an instance variable, not a class variable
# print(Test.b)    # Uncommenting this line will raise an AttributeError
'''

# #Example 5.
'''
class Test:
    a = 10

    def __init__(self):
        self.b = 20

    @classmethod
    def m1(cls):
        cls.a = 33

t = Test()
t2 = Test()
t.m1()
print(t.a,t.b)
print(t2.a,t2.b)
print(Test.a)
'''