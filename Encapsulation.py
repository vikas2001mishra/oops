'''
class Student:
   def __init__(self, name="Tenali Rama", marks=50):
      self.name = name
      self.marks = marks

s1 = Student()
s2 = Student("Krishndev", 25)

print ("Name: {} marks: {}".format(s1.name, s2.marks))
print ("Name: {} marks: {}".format(s2.name, s2.marks))
'''



# 2. Problem Statement:
# Add a new feature in the HR Management System that shows an employee’s salary and the project they are working on.
# For this, we will create a class Employee and add some attributes like name, ID, salary, project, etc.
# As per the requirement, let’s add two required features (methods) – show_sal() to print the salary
# and proj() to print the project working on.


'''
class Employee:
    # constructor
    def __init__(self, name, id, salary, project):
        # data members
        self.name = name
        self.id = id
        self.salary = salary
        self.project = project

    # method to print employee's details
    def show_sal(self):
        # accessing public data member
        print("Name: ", self.name, 'Salary:', self.salary)

    def proj(self):
        print(self.name, 'is working on', self.project)


# creating object of a class
emp = Employee('Rohit', 102, 100000, 'Python')

# calling public method of the class
emp.show_sal()
'''

# Example :
'''
class Employee:
   def __init__(self, name, age):
      self.name = name
      self.age = age

   def display(self):
      print("Employee Name:", self.name)
      print("Employee Age:", self.age)


s = Employee("Kartik Singh", 22)
s.display()
'''



# Example:

'''
class Car:
    def __init__(self, name, mileage):
        self.__name = name  # private attribute
        self.__mileage = mileage  # private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_mileage(self):
        return self.__mileage

    def set_mileage(self, mileage):
        if mileage >= 0:
            self.__mileage = mileage
        else:
            print("Mileage cannot be negative. Setting mileage to 0.")
            self.__mileage = 0


# Create an instance of the Car class
my_car = Car("Toyota", 30)

# Accessing attributes indirectly through getter and setter methods
print("Car Name:", my_car.get_name())
print("Car Mileage:", my_car.get_mileage())

# Updating mileage using setter method
my_car.set_mileage(40)
print("Updated Car Mileage:", my_car.get_mileage())
'''





