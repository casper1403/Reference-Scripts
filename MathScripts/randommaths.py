import random
from statistics import mean

"""Script that calculates the average number of RGN needed to count up to one"""


# Function which sets a counter and a number and returns the times the random function needed to be called to add up to 1
def random_maths():
    counter = 0
    number = 0
    while number <= 1.00:
        number = number + random.random()
        counter+=1
    return counter


# Call the function 1 million times and print the average
numbers = []
for i in range(1_000_000):
    numbers.append(random_maths())

average = round(mean(numbers),4)

print(f"The average amount of numbers generated (based on 1 million trials) is:{average}")
