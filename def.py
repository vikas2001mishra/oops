# Python-OOPs-Concepts

# 1. Classes and Objects

'''
I.Object:- .Everything exist in this world i.e.object, object have behaviour and properties.
           .Object is runtime entity.
  .For Example:-
            obj = Dog()
'''


'''
II.Class:- .Class is a template.
          .class is a blueprint of an object.
          .class is the best example of encapsulation.
          .class is a user defined data type.
'''

# What is --init---

'''
[i] Constructor
[ii] --init--- is a constructor method,and automatically called to allocate memory, when a new object is created.
[iii] Constructor should take atleast one argumentthat is self
'''

# What is Self() ---

'''
[i] self is used to represent the instance(object) of the class.
[ii] self is a Python Provided implicit default variable which is always pointing to current object.
[iii] By using self we can access variables, metheds of corresponding objet.
[iv] In Constructor self should be the first arg (argument).
[v] Self is the 1st argument in the instance method as well.
'''


# Types of variable in Python:
'''
     1.Instance (Object level variable)
     2.Static (Class level variable)
     3.Local (Method level variable)
'''

# 1.Instance variable:-

'''For every object a seperate copy will be created.
		.Where can we declare instance variables:

                #1. Inside constructor by using self variable
                #2. Inside instance method by using self variable
                #3. Outside of the class by using object reference variables
'''

# 2.Static variable:-
'''Only one copy will be created at the class level.
          we are not require to maintain seperate copy of a variable Share the same copy
          One copy of static variable created at the class Level
'''

# How to declare the static variable

'''
#1. Directly create inside the class, Self is not associated 
#2. Inside the constructor by using class name
#3. Inside instance method using class name
#4. Inside class method by using cls variable or class name
#5. Inside static method by using class name
#6. From outside the class as well
'''

# Static variable Only one copy will be created at the class Level
# Instance Variable For every object a seperate copy will be created


# Types of methods:-

'''      1. Instance methods (Object related method)
         2. Static methods
         3. class method
'''

# Instance methods:-
'''
            -> Object related method.
            -> Any method consists of Instance variable-Instance method,
            -> Inside the instance method, First Keyword, i.e. self is compulsory.
'''

# Setter and getter methods:-

'''
.Setter-> To set the value to the Instance variable (mutator method)->(other name Setter).
.getter-> To get the value to the Instance variable.,also known as (Accessor method).
'''

# Static methods:
'''
->Inside method if we are not using instance and static variables.
        ->General utility method
        ->@staticmethed
'''

# class method:-

'''
->Inside the methed Implementation of we are using only static variable (without Instance variables).
->Atleast one Instance variable - instance method.
->Instance method + Static variable -> Both are present (Instance method).
@classmethod # Decorator
cls
we can call class method by using class or object ref.
'''

# Note:-

'''
->Instance methed - (No decorator required)
->class method - @classmethed is (mandatory)
->static method - @staticmethed is (optional)
'''

# Note:-

'''
     ->Instance variables - (Instance method)
     ->static variable - (class method)
     ->Instance + Static- (Instance method)
     ->Instance + local- (Instance method)
     ->static + local (Class method)
     ->local (static method)
'''

# No decorator:-  only two options.
'''   ->Instance method
     ->Static method
'''

# 27.Garbage Collector...

'''
->GC is the part OF Python virtual machine.
->GC is the process of removing any object which are not being used by any other object.
'''

# III. INHERITANCE:-

'''
Inheritance used code reusability.
Inheritance is a relationship between two or more classes.
Inheritance is a real world relationship.

..Inheritance concept into two categories:-
        # Subclass(child class)
        # Superclass(Parent class)

'''

# TYPES OF INHERITANCE:-

'''-> TRICk- SMM HH

1.Single Inheritance.
2.Multilevel Inheritance.
3.Multiple Inheritance.
4.Hierarchical Inheritance.
5.Hybrid Inheritance.
'''

# 1.Single Inheritance.->
'''Single parent, single child.'''

# 2.Multilevel Inheritance:->
'''In multilevel inheritance, features of the base class and the derived class are further inherited into the new derived class. 
     This is similar to a relationship representing a child and a grandfather.'''

# 3.Multiple Inheritance:->
'''When a class is derived from more than one base class it is called multiple Inheritance.'''

# 4.Hierarchical Inheritance.
'''
Hierarchical Inheritance If multiple derived classes are created from the same base, 
this kind of Inheritance is known as hierarchical inheritance. 
'''

# 5.Hybrid Inheritance->
''' Hybrid Inheritance is a combination of multiple Inheritance and multilevel inheritance.'''

# Super()->
'''which can be used to call parent class. Constructor, methods and variables from the child class.'''


# IV. {POLYMORPHISM} ->

'''
           1.polymorphism means many forms.
           2.It is made up of two words poly and forms. It's a geek term. 
           3.Simply put, "Polymorphism means having many forms." 
           4.Polymorphism is an ability by which a message is displayed in many forms.
           5.The process of representing.one form in multiple forms is known as Polymorphism.
           6. The ability to take more than one Form is called polymorphism.

'''


# Real life example of Polymorphism: -
'''So let's look at a real life example. A lady is a teacher in the college. And that woman is a mother or a daughter in her house. 
And there is a customer in the market. Here there are different forms according to the situations of a woman. This
is called polymorphism.'''

# Operator Overloading:-
'''Operator Overloading means giving extended meaning beyond their predefined operational meaning'''

# For example:
'''
            operator + is used to add two integers as well as join two strings and merge two lists. 
            It is achievable because ‘+’ operator is overloaded by int class and str class. 
            You might have noticed that the same built-in operator or function shows different behavior for objects of different classes, 
            this is called Operator Overloading. 
'''


# Method Overloading:-

''' Python does not support method Overloading.'''
'''Two or more methods have the same name but different Parameters or different  types of parameters 
i.e. called method overloading.'''

# Method Overriding:->
'''whenever, we writing method name with Same Signeture in parent and Child class called method overriding.'''
'''method Overriding avoids duplication of code.'''

# Super method:->
'''n Python, the super() function is used to refer to the parent class or superclass.'''
'''It allows you to call methods defined in the superclass from the subclass.'''

# V. Encapsulation:->
'''Encapsulation means, binding variables and methods together into a single unit i.e. called Encapsulation.'''


# VI. Abstraction:-
'''Abstraction is hiding the unnecessary data & showing only essential part.'''
'''
Abstraction in python is defined as a process of handling complexity by hiding 
unnecessary information from the user. 
'''

