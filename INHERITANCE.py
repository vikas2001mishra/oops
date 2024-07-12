#Example 1.

'''
class Car:
    def __init__(self, name, model, color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("Car Name:", self.name)
        print("Car Model:", self.model)
        print("Car Color:", self.color)

# Create an instance of the Car class
c = Car("Maruti 800", 800, "White")

# Call the getinfo method to print information about the car
c.getinfo()
'''

#Example 2.

'''
class Car:
    def __init__(self,name,model,color):
        self.name = name
        self.model = model
        self.color = color

    def getinfo(self):
        print("Car Name:",self.name)
        print("Car Model:",self.model)
        print("car color:",self.color)

class Employee:
    def __init__(self,eno,ename,car):
        self.eno = eno
        self.ename = ename
        self.car = car

    def empinfo(self):
        print("Employee NO:",self.eno)
        print("Employee Name:",self.ename)
        print("car information--->")
        self.car.getinfo()

c=Car("Maruti 800",800,"White")
e = Employee(100,"Satish",c)
e.empinfo()
'''

# TYPES OF INHERITANCE:-
# -> TRICk- SMM HH
#
# 1.Single Inheritance.
# 2.Multilevel Inheritance.
# 3.Multiple Inheritance.
# 4.Hierarchical Inheritance.
# 5.Hybrid Inheritance.

# 1.Single Inheritance.->
#                       Single parent, single child.

'''
class P:
    def  m1(self):
        print("Parent method")
class C(P):
    def m2(self):
        print("Child method")
c=C()
c.m1()
c.m2()
'''

# 2.Multilevel Inheritance:->
   #  This is similar to a relationship representing a child and a grandfather.

'''
class P:
    def m1(self):
        print("Parent method")
class C(P):
    def m2(self):
        print("Child method")
class CC(C):
    def m3(self):
        print("Sub-child method")
cc=CC()
cc.m1()
cc.m2()
cc.m3()
'''

# 3.Multiple Inheritance:->
#        -> When a class is derived from more than one base class it is called multiple Inheritance.

'''
class P1:
    def m1(self):
        print("Parent 1 method")
class P2:
    def m2(self):
        print("Parent 2 method")
class C(P1,P2):
    def m3(self):
        print("child method")
c = C()
c.m1()
c.m2()
c.m3()
'''

# 4.Hierarchical Inheritance.
   #Hierarchical Inheritance If multiple derived classes are created from the same base,
      # this kind of Inheritance is known as hierarchical inheritance.

'''
class P:
    def m1(self):
        print("Parent class")
class C1(P):
    def m2(self):
        print("Child 1 method")
class C2(P):
    def m3(self):
        print("Child 2 method")

c = C1()
c.m1()
c.m2()
#c1.m3()
c = C2()
c.m3()
'''

# 5.Hybrid Inheritance->
#            -> Hybrid Inheritance is a combination of multiple Inheritance and multilevel inheritance.


'''
class A:
    def m1(self):
        print("Class A method")
class B(A):
    def m2(self):
        print("Class B method")
class C(A):
    def m3(self):
        print("Class C method")
class D(B,C):
    def m4(self):
        print("Class D method")

d = D()
d.m1()
d.m2()
d.m3()
d.m4()
'''


# Super()->
#       which can be used to call parent class. Constructor, methods and variables from the child class.


'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class Student:
    def __init__(self,name,age,Rollno,marks):
        self.name = name
        self.age = age
        self.Rollno = Rollno
        self.marks = marks

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Roll no:",self.Rollno)
        print("Marks:",self.marks)

s = Student("Aman",22,3,68)
s.display()
'''

# Example:

'''
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display1(self):
        print("Name:",self.name)
        print("Age:",self.age)


class Student(Person):
    def __init__(self,name,age,rollno,marks):
        super().__init__(name,age)
        self.rollno = rollno
        self.marks = marks

    def display2(self):
        super().display1()
        print("Rollno:",self.rollno)
        print("marks:",self.marks)
s = Student("Rahul",22,46,87)
s.display2()
#s.display1()
'''



# Example:

'''
# Parent class (superclass)
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")


# Child class (subclass) inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"


# Create instances of the child classes
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Call the speak method on each instance
print(dog.speak())  
print(cat.speak())  
'''