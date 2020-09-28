import random
import numpy as np

"""Script showing different ways to generate random numbers"""

# Generate random float between 0 and 1
a = random.uniform(0,1)

# Generate random integer between x and y
b = np.random.randint(0,100)
c  = random.randint(0,100)


print(a, "\n", b ,"n", c)
