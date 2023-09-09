import random
num = random.randint(1, 10)
while True:
    ans = float(input("Please enter a number:\n"))
    if ans == num:
        print("Correct")
        break
    elif ans > num:
        print("Too high")
    elif ans < num:
        print("Too low")