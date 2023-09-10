# import time
import random
n = int(input("Enter the number of random points to generate:"))
# start_time = time.time()
i = 0
circle = 0
while i < n:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    d = x ** 2 + y ** 2
    if d < 1:
        circle+=1
    i+=1
pi = 4 * circle / n
print(f"Approximation of pi using {n} points: {pi}")
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f"Time used: {elapsed_time:.2f} sec")