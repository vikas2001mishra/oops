# Example 1.Here’s a simple example a static method in Python:

'''
class MathOperations:
    @staticmethod
    def add(x, y):
        return x + y

# Using the static method without creating an instance
result = MathOperations.add(5, 3)
print(result)
'''

# Example 2.

'''
class Rahulmarks:
    @staticmethod
    def add(x,y):
        print('the sum is:',x+y)
    @staticmethod
    def product(x,y):
        print('the product is:',x*y)
    @staticmethod
    def average(x,y):
        print('the avg is:',(x+y)/2)
Rahulmarks.add(10,20)
Rahulmarks.product(10,20)
Rahulmarks.average(10,20)
'''

# Example 3.Passing The members of one class to another ......?
'''
class Employee:
    def __init__(self, eno, ename, esal):
        self.eno = eno
        self.ename = ename
        self.esal = esal

    def display(self):
        print("Employee No:", self.eno)
        print("Employee Name:", self.ename)
        print("Employee Salary:", self.esal)

class Test:
    @staticmethod
    def modify(emp):
        emp.esal += 10000
        emp.display()

# Create an Employee object
e = Employee(100, "Rahul", 15000)

# Modify the employee's salary and display the details
Test.modify(e)
'''


# Example 4.
'''
class Test:
    def Modify(emp):
        print('Hello')
e = Test()
e.Modify() #Instance
Test.Modify(56) #Static Method
'''




