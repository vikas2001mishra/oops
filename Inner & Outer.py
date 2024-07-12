#Ineer Classes:
 # Classes Inside the another classes.
 # Without exixting outer class inner class is of no use.
# Example 1:

'''
class Outer:
    def __init__(self):
        print("outer class object creation...")

    class Inner:
        def __init__(self):
            print("Inner class object creation...")

        def m1(self):
            print("Inner Class Method")

#i = Outer().Inner().m1()
o = Outer()
i = o.Inner()
i.m1()
'''


# Example 2:
'''
class Outer:
    def __init__(self):
        print("outer class object creation...")
    class Inner:
        def __init__(self):
            print("Inner class object creation...")
        class InnerInner:
            def __init__(self):
                print("Inner Inner clas object creation...")
            def m1(self):
                print("Inner Inner class Method")
i =Outer().Inner().InnerInner().m1()
'''

# Example 3:
'''
class Human:
    def __init__(self):
        self.name = 'Rahul'
    def display(self):
        print("Hello",self.name)
h=Human()
h.display()
'''

# Example 4.

'''
class Human:
    def __init__(self):
        self.name = 'Rahul'
        self.head = self.Head()
        self.brain = self.head.Brain()

    def display(self):
        print("Hello",self.name)
        self.head.talk()
        self.brain.think()

    class Head:
        def talk(self):
            print("Talking.....")
        class Brain:
            def think(self):
                print("Thinking...")
h=Human()
h.display()
h.Head()
'''

# Example 5.defines a Customer class and a DOB class to represent a customer's date of birth.

'''
class Customer:
    def __init__(self, name, dd, mm, yyyy):
        self.name = name
        self.dob = DOB(dd, mm, yyyy)

    def display(self):
        print('Customer Name:', self.name)
        self.dob.display()

class DOB:
    def __init__(self, dd, mm, yyyy):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

    def display(self):
        print('DOB={}/{}/{}'.format(self.dd, self.mm, self.yyyy))

# Create a Customer object
c = Customer('Ratnesh', 10, 11, 2010)

# Display the customer details
c.display()
'''

# Example 6:
# defines a Test class with a method m1 that performs and prints arithmetic operations
# (sum, difference, multiplication, and division) on three different pairs of numbers.

class Test:
    def m1(self):
        a, b = 10, 20
        print('For a =', a, 'and b =', b)
        print('The sum is:', a + b)
        print('The diff is:', a - b)
        print('The mul is:', a * b)
        print('The div is:', a / b)
        print()

        a, b = 100, 200
        print('For a =', a, 'and b =', b)
        print('The sum is:', a + b)
        print('The diff is:', a - b)
        print('The mul is:', a * b)
        print('The div is:', a / b)
        print()

        a, b = 1000, 2000
        print('For a =', a, 'and b =', b)
        print('The sum is:', a + b)
        print('The diff is:', a - b)
        print('The mul is:', a * b)
        print('The div is:', a / b)
        print()

# Create an instance of the Test class
t = Test()

# Call the method m1
t.m1()
