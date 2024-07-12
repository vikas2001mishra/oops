#Example 1.

'''
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    def display(self):
        print('hi',self.name)
        print('your marks are:',self.marks)
    def grade(self):
        if self.marks>=60:
            print("you got 1st div.")
        elif self.marks>=50:
            print("yor got 2nd div.")
        elif self.marks>=33:
            print("you got 3rd div.")
        else:
            print("you did not pass")
s = Student("Rahul",69)
s.display()
s.grade()
'''

#Example 2.

'''
class MyClass:
    def __init__(self, value):
        self.value = value  # Instance variable

    def display_value(self):
        print(f'Value: {self.value}')

    def increment_value(self, increment):
        self.value += increment

# Create an instance of MyClass
obj = MyClass(5)

# Call instance methods on the instance
obj.display_value()  # Output: Value: 5

obj.increment_value(3)
obj.display_value()  # Output: Value: 8
'''

#Example 3.
'''
class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


p = Person('Ram')
p.say_hi()
'''


