#Example 1.
# class Employee:
#     '''This is a class which will calculate the salary of an employee'''
# print(Employee.__doc__)
# help(Employee)

#Example 2.
#Class

'''class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return "Woof!"
#object
my_dog = Dog("Buddy", 3)
print(my_dog.name)  # Output: Buddy
print(my_dog.bark())  # Output: Woof!
'''


#Example 3. the salaries are printed.
'''
class Employee:
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary

vikas = Employee('vikas', 'mishra', 50000)
Rohan = Employee('Rohan', 'kumar', 40000)

'''

#Example 4. Other Method:-

'''
class Employee:
    def __init__(self,fname,lname,salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
    def info(self):
        print(self.fname)
        print(self.lname)
        print(self.salary)
emp = Employee("Rahul","Sharma",1000)
emp.info()
'''

#Example 5.Employee Salary Increment?

'''
class Employee:
    increment = 2.5
    def __init__(self,fname,lname,salary):
     self.fname = fname
     self.lname = lname
     self.salary = salary
    def increase(self):
        self.salary = self.salary * Employee.increment
mukesh = Employee("mukesh","mishra",5000)
mukesh.increase()
print(mukesh.salary)
'''

#Example 6. celsius to fahrenheit?

'''
def ctof(c):
    f = (c*9/5)+32
    print(f)
ctof(10)
ctof(20)
ctof(30)
'''

# Other Method:

'''
class Ctof:
    def __init__(self,c):
        self.c = c
    def ctof(self):
        f = (self.c*9/5)+32
        print(f)

f1 = Ctof(12)
f2 = Ctof(14)
f3 = Ctof(16)
f1.ctof()
f2.ctof()
f3.ctof()
'''

#Example 7. Employee,name,employeeid,salary:-

'''
class Employee:
    def __init__(self,name,employeeid,salary):
        self.name = name
        self.employeeid = employeeid                 # These three are instance variables.
        self.salary = salary
    def talk(self):       #its not a function ,talk is a method
        print("hello my name is:",self.name)
        print("hello my employeeid is:",self.employeeid)
        print("hello my salary is:",self.salary)
emp1 = Employee("Suresh",1234,56789)
emp2 = Employee("Ramesh",1290,56700)
emp1.talk()
emp2.talk()
'''


#Example 8.Movie Example:
'''
class Movie:
    def __init__(self,name,hero,heroine,rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
    def info(self):
        print("movie name:",self.name)
        print("movie hero:",self.hero)
        print("movie heroine:",self.heroine)
        print("movie rating:",self.rating)
mov = Movie("PK","AK","AS",10)
mov.info()
'''

#Example 9.Movie Example through for loop:-

'''
class Movie:
    def __init__(self,name,hero,heroine,rating):
        self.name = name
        self.hero = hero
        self.heroine = heroine
        self.rating = rating
    def info(self):   #info is method
        print("movie name:",self.name)
        print("movie hero:",self.hero)
        print("movie heroine:",self.heroine)
        print("movie rating:",self.rating)
movies = [Movie("PK","AK","AS",10),Movie("AB","CD","EF",10),Movie("GH","IJ","KL" ,6),Movie("MN","OP","QR",0 )]
for mov in movies:
    mov.info()
'''

