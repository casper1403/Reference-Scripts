import random
import matplotlib.pyplot as plt

""" Function that plots a histogram of random values and the percentage < 40 and > 60.


Casper van der Vliet
11052953"""


# Function to calculate the sum of 100 random numbers
def sum_random_numbers():
    number = 0
    for i in range(100):
        number = number + random.random()
    return number

# Loop 10000 times and add averages to list
averages = []
for i in range(10_000):
    averages.append(sum_random_numbers())


# Two lists to catch the values over 60 and under 40 in a for loop
forty = []
sixty = []
for i in averages:
    if i < 40:
        forty.append(i)
    if i > 60:
        sixty.append(i)


# Print te percentage
print(f"Number of experiments where the sum was < 40: {(len(forty)/ len(averages))}")
print(f"Number of experiments where the sum was > 60: {(len(sixty)/ len(averages))}")

# Plot the Histogram
plt.xlim(30, 70)
plt.hist(averages, bins=50)
plt.show()
