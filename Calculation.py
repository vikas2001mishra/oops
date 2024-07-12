# Make Caluclator:

# 1.Add,Sub,Mul,Div of two no.

'''
class Calculator:
    def __init__(self):
        self.a = 10
        self.b =20

    def m1(self):
        print("Add:",self.a+self.b)

    def m2(self):
        print("Sub:",self.a-self.b)

    def m3(self):
        print("Mul:",self.a*self.b)

    def m4(self):
        print("Div:",self.a/self.b)

result = Calculator()
result.m1()
result.m2()
result.m3()
result.m4()
'''

# 2.Add,Sub,Mul,Div of three no.

'''
class Calculator:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def m1(self):
        print('Add:',self.a + self.b + self.c)
    def m2(self):
        print('Sub:',self.a - self.b - self.c)
    def m3(self):
        print('Mul:',self.a * self.b * self.c)
    def m4(self):
        print('Div',self.a / self.b / self.c)
t = Calculator()
t.m1()
t.m2()
t.m3()
t.m4()
'''

# 3. Calculation take the User Input:

'''
class Calculation1:
    def Sum(self, a, b):
        return a + b

class Calculation2:
    def sub(self, a, b):
        return a - b

class Calculation3:
    def Mul(self, a, b):
        return a * b

class Div(Calculation1, Calculation3):
    def Divide(self, a, b):
        return a / b

# Create instances of the classes
calc1 = Calculation1()
calc2 = Calculation2()
calc3 = Calculation3()
div = Div()

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform calculations using the methods of the classes
print("Sum:", calc1.Sum(num1, num2))
print("Sub:", calc2.sub(num1, num2))
print("Mul:", calc3.Mul(num1, num2))
print("Div:", div.Divide(num1, num2))
'''

# 4. Another Calculation Example:

'''
class P:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

class C1(P):
    def subtract(self):
        return self.num1 - self.num2

class C2(P):
    def multiply(self):
        return self.num1 * self.num2

class C3(P):
    def divide(self):
            return self.num1 / self.num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
r = P(num1, num2)

c1 = C1(num1, num2)
c2 = C2(num1, num2)
c3 = C3(num1, num2)

# Display the results
print("\nResults:")
print("Sum:", r.add())
print("Subtraction:", c1.subtract())
print("Multiplication:", c2.multiply())
print("Division:", c3.divide())
'''

# Arithmetic Operation in oops concept in python:

'''
class Arith:
    def add(self, a, b):
        print("Addition by Arith:=", a + b)

    def sub(self, a, b):
        print("Subtraction by Arith:=", a - b)

    def div(self, a, b):
        print("Division by Arith:=", a / b)

    def multi(self, a, b):
        print("Multiplication by Arith:=", a * b)



class Arith1(Arith):
    def add(self, a, b):
        print("Addition by Arith1:=", a + b)

    def sub(self, a, b):
        print("Subtraction by Arith1:=", a - b)

    def div(self, a, b):
        print("Division by Arith1:=", a / b)

    def multi(self, a, b):
        print("Multiplication by Arith1:=", a * b)


class Arith2(Arith):
    def add(self, a, b):
        print("Addition by Arith2:=", a + b)

    def sub(self, a, b):
        print("Subtraction by Arith2:=", a - b)

    def div(self, a, b):
        print("Division by Arith2:=", a / b)

    def multi(self, a, b):
        print("Multiplication by Arith2:=", a * b)



# result1 = Arith()
# result1.add(10, 20)
# result1.sub(60, 20)
# result1.multi(10, 20)
# result1.div(100, 20)

# result2 = Arith()
# result2.add(10, 2)
# result2.sub(80, 20)
# result2.multi(90, 20)
# result2.div(70, 20)

# result3 = Arith()
# result3.add(10, 2)
# result3.sub(80, 20)
# result3.multi(90, 20)
# result3.div(70, 20)

res1 = Arith()
res1.add(10,20)
res2 = Arith2()
res2.add(111,222)
'''

# Some other Example:-

'''
class Calculator:
    def __init__(self):
        self.a = 10
        self.b = 20
        self.c = 30
    def m1(self):
        print('Add:',self.a + self.b + self.c)
    def m2(self):
        print('Sub:',self.a - self.b - self.c)
    def m3(self):
        print('Mul:',self.a * self.b * self.c)
    def m4(self):
        print('Div',self.a / self.b / self.c)
t = Calculator()
t.m1()
t.m2()
t.m3()
t.m4()
'''

# Some other Example:-
'''
class Calculation:
    def sum(self, a, b):
        return a + b

class Calculation2:
    def sub(self, a, b):
        return a - b

class Calculation3:
    def mul(self, a, b):
        return a * b

class Calculation4(Calculation, Calculation2, Calculation3):
    def divide(self, a, b):
        return a / b

# Taking user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Creating an instance of Calculation4
calc = Calculation4()

# Performing calculations
print("Sum:", calc.sum(num1, num2))
print("Sub:", calc.sub(num1, num2))
print("Mul:", calc.mul(num1, num2))
print("Div:", calc.divide(num1, num2))
'''


# Some other Example:-
'''
class P:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

class C1(P):
    def subtract(self):
        return self.num1 - self.num2

class C2(P):
    def multiply(self):
        return self.num1 * self.num2

class C3(P):
    def divide(self):
            return self.num1 / self.num2

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
r = P(num1, num2)

c1 = C1(num1, num2)
c2 = C2(num1, num2)
c3 = C3(num1, num2)

# Display the results
print("\nResults:")
print("Sum:", r.add())
print("Subtraction:", c1.subtract())
print("Multiplication:", c2.multiply())
print("Division:", c3.divide())
'''

