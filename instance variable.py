# How to access the instance variable.
   # Within the class by using self.


#Example 1.
'''
class Test:
    def __init__(self):
        self.a = 20
        self.b = 30
    def m1(self):
        print(self.a)
        print(self.b)
t = Test()
t.m1()
#print(t.a)
#print(t.b)
'''

#Example 2. How to delete the instance variables
#del self.variablename within the class

'''
class Test:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
        self.d = 40

    def m1(self):
        del self.b

#Create an instance of the Test class
t = Test()

#Print the instance variables before deletion
print("Before deletion:", t.__dict__)

#Call the method m1 to delete the instance variable 'b'
t.m1()

#Print the instance variables after deletion
print("After deletion:", t.__dict__)
'''

#Example 3. Questions: xthe subsequent operations:
#[i] What is the output of the first print(t.__dict__) statement before calling the m1 method?
#[ii] What changes occur to the instance variables when the m1 method is called?
#[iii] What is the output of the second print(t.__dict__) statement after calling the m1 method?
#[iv] What is the output of the third print(t.__dict__) statement after modifying the instance variable b?
#[v] What is the output of the final print(t.__dict__) statement after adding the new instance variable c?

'''
class Test:

    def __init__(self):  # Correct the constructor method name
        self.a = 10

    def m1(self):
        self.a = 777
        self.b = 888

#Create an instance of the Test class
t = Test()

#Print the instance variables before calling m1
print(t.__dict__)  # Note: Use double underscores for __dict__

#Call the method m1 to modify instance variables
t.m1()

#Print the instance variables after calling m1
print(t.__dict__)

#Modify instance variable 'b' and add new instance variable 'c'
t.b = 1000

#Print the instance variables after modifying 'b'
print(t.__dict__)

#Add new instance variable 'c'
t.c = 2000

#Print the instance variables after adding 'c'
print(t.__dict__)
'''

#Example 4. write Fibonacci series up to n?
'''
def fib(n):
    # """"Print a Fibonacci series up to n.""""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a + b
fib(10)
'''

#Example 5.return Fibonacci series up to n?

'''
def fib2(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result

f100 = fib2(100)    # call it
print(f100)
'''




