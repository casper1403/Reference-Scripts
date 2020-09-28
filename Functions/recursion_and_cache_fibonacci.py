from functools import lru_cache

""" Function which returns the fibonacci sequance, the function
make use of the lru_cache function which acts as a temporary memory
storage for the numbers in the fib(n)  function

The function makes use of recursion to output the sequence"""



# @lru_cache(maxsize = 1000)
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n > 2:
        return fib(n-1) + fib(n - 2)

for n in range(1, 150000):
    print(n, ":", fib(n))
