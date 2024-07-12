# Example 1.

'''
class Test:
    a = 100  # static variable

    def __init__(self):
        self.b = 200

    def m1(self):
        self.c = 300

    @classmethod
    def m2(cls):
        cls.d = 400
        Test.e = 500

    @staticmethod
    def m3():
        Test.f = 600

# Create an instance of Test
t = Test()
print(Test.__dict__)  # Initial state

# Call the instance method m1
t.m1()
print(Test.__dict__)  # After calling m1

# Call the class method m2
t.m2()
print(Test.__dict__)  # After calling m2 once

# Call the class method m2 again
t.m2()
print(Test.__dict__)  # After calling m2 again

'''
#Example 2.Here's how you can define and use static variables in Python:

'''
class MyClass:
    # This is a static variable
    static_variable = 42

    def __init__(self, value):
        # This is an instance variable
        self.instance_variable = value

    def display(self):
        print(f'Static Variable: {MyClass.static_variable}')
        print(f'Instance Variable: {self.instance_variable}')

# Create instances of the class
obj1 = MyClass(1)
obj2 = MyClass(2)

# Access the static variable through the class
print(MyClass.static_variable)  # Output: 42

# Access the static variable through an instance
print(obj1.static_variable)  # Output: 42
print(obj2.static_variable)  # Output: 42

# Modify the static variable
MyClass.static_variable = 100

# The change is reflected in all instances
print(obj1.static_variable)  # Output: 100
print(obj2.static_variable)  # Output: 100

# Modify an instance variable
obj1.instance_variable = 10

# The change is reflected only in that instance
print(obj1.instance_variable)  # Output: 10
print(obj2.instance_variable)  # Output: 2
'''


#Example 3.How to access the Static Variable...
    #1.Inside the constructor Either by self or by class name
    #2. Inside the Instance method Either by self or class name
    #3. Inside the class method Either by cls or by class name
    #4. Inside the static method By class name
    #5. Outisde the class Either by object ref or by class name


'''
class Test:
    a = 10
    def __init__(self):
        print(self.a)           #constuctor method
        print(Test.a)

    def m1(self):
        print(self.a)           #Instance method
        print(Test.a)

    @classmethod
    def m2(cls):
        print(cls.a)           #class method
        print(Test.a)

    @staticmethod
    def m3():                  #Static method
        print(Test.a)
t = Test()
t.m1()
t.m2()
t.m3()
'''

#Example 4.update value?:

'''
class Test:
    a = 10
    def __init__(self):
        Test.a = 20
t = Test()
print(Test.a)
'''

#Example 5. Where we can modify the value of Static variables:
        #By using the class name (Inside or outside the class)
	   #Inside the class method by using cls variable also.

'''
class Test:
    a = 10  # Class variable

    def __init__(self):
        Test.a = 888  # Modify class variable in the constructor

    def m1(self):
        Test.a = 10000  # Modify class variable in an instance method

    @classmethod
    def m2(cls):
        Test.a = 9090  # Modify class variable using the class name
        cls.a = 2222   # Modify class variable using cls

    @staticmethod
    def m3():
        Test.a = 22122  # Modify class variable in a static method

# Create an instance of the Test class
t = Test()
print(Test.a)  # Should print 888 after the constructor is called

t.m1()
print(Test.a)  # Should print 10000 after calling instance method m1

t.m2()
print(Test.a)  # Should print 2222 after calling class method m2

t.m3()
print(Test.a)  # Should print 22122 after calling static method m3

Test.a = 44322  # Modify class variable directly using the class name
print(Test.a)  # Should print 44322
'''

#Example 6.

'''
class Test:
    a = 10
    def __init__(self):
        Test.a = 888
    def m1(self):
        Test.a = 999
t = Test()
print(Test.a)
t.m1()
print(Test.a)

'''

#Example 7.

'''
class Test:
    # Static variable
    a = 10

    def __init__(self):
        # Modifying the static variable
        Test.a = 1000

        # Local variable (not used elsewhere)
        a = 100

        # Instance variable
        self.a = 90

        # Printing the instance variable
        print(self.a)  # Output: 90

        # Printing the static variable
        print(Test.a)  # Output: 1000

    def m1(self):
        # Local variable
        b = 10
        print(b)  # Output: 10

# Create an instance of the class
t = Test()

# Call the m1 method
t.m1()
'''


