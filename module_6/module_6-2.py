import random
def dice(n):
    return random.randint(1,n)

# main program
n = int(input("Please define number of faces of the dice:"))
while True:
    i = dice(n)
    if i == n:
        print(f"The number is '{n}', program finish.")
        break
    else:
        print(f"The number is '{i}', dice again.")