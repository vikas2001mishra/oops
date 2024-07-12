# Example 1:

'''
from abc import ABC,abstractmethod
class Animal:
    def sleep(self):
        print("I am going to sleep in a while")

    @abstractmethod
    def sound(self):
        print("This function is for defining the sound by any animal")
        pass

class Snake(Animal):
    def sound(self):
        print("I can hiss")

class Dog(Animal):
    def sound(self):
        print("I can bark")

class Lion(Animal):
    def sound(self):
        print("I can roar")

class Cat(Animal):
    def sound(self):
        print("I can meow")

c = Cat()
c.sleep()
c.sound()

c = Snake()
c.sound()
'''


# Example :

'''
from abc import ABC, abstractmethod


# Abstract class
class Shape(ABC):
    # Abstract method (must be overridden in subclass)
    @abstractmethod
    def area(self):
        pass

    # Abstract method (must be overridden in subclass)
    @abstractmethod
    def perimeter(self):
        pass


# Concrete subclass Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Concrete subclass Square
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return 4 * self.side


# Create instances of Circle and Square
c = Circle(5)
s = Square(4)

# Calling methods without worrying about implementation details
print("Area of Circle:", c.area())
print("Perimeter of Circle:", c.perimeter())
print("Area of Square:", s.area())
print("Perimeter of Square:", s.perimeter())
'''