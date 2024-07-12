#Example 1.

'''
class Test:
    a = 777
    def __init__(self):
        self.a = 888
t = Test()
print(t.a) #Instance variable
print(Test.a) #Static Variable

'''

#Example 2.

'''
class ExampleClass:
    # Static variable
    static_variable = 'I am a static variable'

    def __init__(self, instance_value):
        # Instance variable
        self.instance_variable = instance_value

    def display_variables(self):
        print(f'Static Variable: {ExampleClass.static_variable}')
        print(f'Instance Variable: {self.instance_variable}')

# Create instances of the class
obj1 = ExampleClass('Instance 1')
obj2 = ExampleClass('Instance 2')

# Display the variables for both instances
obj1.display_variables()
obj2.display_variables()

# Modify the static variable
ExampleClass.static_variable = 'Static variable has changed'

# Modify an instance variable
obj1.instance_variable = 'Modified Instance 1'

# Display the variables again to see the changes
obj1.display_variables()
obj2.display_variables()
'''