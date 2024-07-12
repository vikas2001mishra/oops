# Example 1.Basic Example:

'''
import gc

# Create a function to demonstrate garbage collection
def demo_garbage_collection():
    # Create a circular reference
    x = []
    y = []
    x.append(y)  # x references y
    y.append(x)  # y references x

    # Delete references to break the cycle
    del x, y

    # Force garbage collection (optional in normal usage)
    gc.collect()

    # At this point, the circular reference is collected

# Call the function to demonstrate garbage collection
demo_garbage_collection()

'''

# Example 2. Resource Management example:

'''
import numpy as np
import gc


# Function to demonstrate resource management with garbage collection
def process_large_data():
    # Load a large dataset into memory
    data = np.random.rand(10000, 10000)

    # Perform some operations
    processed_data = data * 2

    # Perform further operations

    # Explicitly free up memory by deleting references
    del data, processed_data

    # Force garbage collection to reclaim memory
    gc.collect()


# Call the function to process large data and manage memory
process_large_data()
'''


# Example 3.

'''
import gc
print(gc.isenabled())
gc.disable()
print(gc.isenabled())
gc.enable()
print(gc.isenabled())
'''


