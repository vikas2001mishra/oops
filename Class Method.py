# Example 1.Here's how you define and use a class method in Python:

'''
class MyClass:
    class_variable = 10  # Class variable

    def __init__(self, value):
        self.value = value  # Instance variable

    @classmethod
    def class_method(cls, x):
        print(f"Class method called with {x}")
        cls.class_variable = x  # Modifying class variable

# Using the class method without an instance
MyClass.class_method(50)

# Accessing modified class variable
print(MyClass.class_variable)  # Output: 50

# Creating an instance of MyClass
obj = MyClass(20)

# Accessing instance variable
print(obj.value)  # Output: 20

'''

# Example 2:

'''
class Employee:
    total_emp = 10
    @classmethod
    def totemp(cls,compname):
        print("{} has total {} employees".format(compname,cls.total_emp))
Employee.totemp('TCS')
'''

# Example 3:

'''
class Test:
    count = 0
    def __init__(self):
        Test.count = Test.count+1
    @classmethod
    def noofobj(cls):
        print("The no of object created",Test.count)
t1 = Test()
t2 = Test()
t3 = Test()
Test.noofobj()
'''