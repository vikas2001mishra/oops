# Example 1.

'''
class India():
	def capital(self):
		print("New Delhi is the capital of India.")

	def language(self):
		print("Hindi is the most widely spoken language of India.")

	def type(self):
		print("India is a developing country.")

class USA():
	def capital(self):
		print("Washington, D.C. is the capital of USA.")

	def language(self):
		print("English is the primary language of USA.")

	def type(self):
		print("USA is a developed country.")

obj_ind = India()
obj_usa = USA()
for country in (obj_ind, obj_usa):
	country.capital()
	country.language()
	country.type()
'''

# # Example 2.
'''
class Women:
    def Home(self):
        print("Home:","Sister,Daughter,Wife,Mother etc.")

    def College(self):
        print("College:","Teacher")

    def Market(self):
        print("Market:","Customer")

w = Women()
w.Home()
w.College()
w.Market()
'''


# Example:

'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print("Student Name:", self.name)
        print("Student Age:", self.age)


# Create an instance of the Student class
s = Student("Vikrant", 22)

# Call the info method to display student information
s.info()
'''

# Example:
'''
class Bird:
    def intro(self):
        print("There are many types of birds.")

    def flight(self):
        print("Most of the birds can fly but some cannot.")


class Sparrow(Bird):
    def flight(self):
        print("Sparrows can fly.")


class Ostrich(Bird):
    def flight(self):
        print("Ostriches cannot fly.")


# Create instances of each class
obj_bird = Bird()
obj_spr = Sparrow()
obj_ost = Ostrich()

# Call methods on each instance
obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
'''

# Operator Overloading:-

'''
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __add__(self, other):
        return self.pages+other.pages
b1 = Book(100)
b2 = Book(200)        #Magic Method
print(b1+b2)
'''

# Example:

'''
class Book:
    def __init__(self,pages):
        self.pages = pages
    def __mul__(self, other):
        return self.pages*other.pages
b1 = Book(100)
b2 = Book(200)        #Magic Method
print(b1*b2)
'''

# Method Overloading:-

'''
class Test:
    def m1(self):
        print("Zero args method")
    def m1(self,a):
        print("One args method")
    def m1(selfa,b):
        print("Two args method")
t = Test()
t.m1(10)
'''

# Example:

'''
class Test:
    def sum1(self,a = None,b = None,c = None):
        if a!= None and b!= None and c!= None:
            print("The sum of three value is:",a+b+c)
        elif a!=None and b!=None:
            print("The sum of two numbers:",a+b)
        elif a!=None:
            print("The sum of one numbers is:",a)
        else:
            print("At least provide one value")
t=Test()
t.sum1()
t.sum1(10)
t.sum1(10,20)
t.sum1(10,20,30)
'''

# Method Overriding:->

'''
class P:
    def property(self):
        print('cash+gold+car+house')
class C(P):
    pass
c = C()
c.property()
'''

# Other Example.

'''
class P:
    def property(self):
        print("Gold", "money", "car")

class C(P):
    def job(self):
        print("Software Engineer")

c = C()
c.property()  # Calls the method from the parent class
c.job()       # Calls the method from the child class
'''


# Other Example.


'''
class Animal:
    def sound(self):
        print("This is a generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Dog:","Bark")

class Cat(Animal):
    def sound(self):
        print("Cat:","Meow")

# Create instances of Dog and Cat
dog = Dog()
cat = Cat()

# Call the sound method on each instance
dog.sound()  # Output: Bark
cat.sound()  # Output: Meow
'''

# Super method:->

#Example Using super()

'''
class Animal:
    def sound(self):
        print("This is a generic animal sound")

class Dog(Animal):
    def sound(self):
        super().sound()
        print("Dog:","Bark")

# Create an instance of Dog
dog = Dog()

# Call the sound method
dog.sound()
'''

# Other Example:

'''
class P:
    def __init__(self):
        print("Parent constructor")
class C(P):
    def __init__(self):
        #super(). __init__()          #Super method
        print("Child constuctor")
c = C()
'''
