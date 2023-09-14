import random
def dice():
    return random.randint(1,6)

# main program
while True:
    i = dice()
    if i == 6:
        print("The number is '6', program finish.")
        break
    else:
        print(f"The number is '{i}', dice again.")