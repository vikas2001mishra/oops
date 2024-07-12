# Here's how you define a getter method in Python:
'''
class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute with double underscore prefix

    def get_value(self):
        return self.__value

# Creating an instance of MyClass
obj = MyClass(10)

# Using the getter method to retrieve the attribute value
print(obj.get_value())  # Output: 10

'''

# Here's how you define a setter method in Python:

'''
class MyClass:
    def __init__(self, value):
        self.__value = value  # Private attribute with double underscore prefix

    def get_value(self):
        return self.__value

    def set_value(self, new_value):
        if new_value >= 0:  # Example validation logic
            self.__value = new_value
        else:
            print("Error: Value must be non-negative.")

# Creating an instance of MyClass
obj = MyClass(10)

# Using the getter method to retrieve the attribute value
print(obj.get_value())  # Output: 10

# Using the setter method to modify the attribute value
obj.set_value(20)
print(obj.get_value())  # Output: 20

# Trying to set a negative value (validation example)
obj.set_value(-5)  # Output: Error: Value must be non-negative.
print(obj.get_value())  # Output: 20 (value remains unchanged)
'''



#defines a Student class with methods to set and get student names and marks,
# and then uses these methods to create a list of students and display their details.

class Student:
    def setName(self,name):
        self.name = name
    def getName(self):
        return self.name

    def setMarks(self,marks):
        self.marks = marks
    def getMarks(self):
        return self.marks

students_list = []
num_students = int(input("Enter the number of the Student:"))
for i in range(num_students):
    s = Student()
    name = input("Enter the Student name:")
    marks = input("Enter marks:")
    s.setName(name)
    s.setMarks(marks)
    students_list.append(s)

for s in students_list:
    print("Student Name:",s.getName())
    print("Student Marks:",s.getMarks())
    print()