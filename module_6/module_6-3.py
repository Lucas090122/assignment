def exchange(a):
    return a * 3.785


# main program
print("This program transfer US gallons to liters, enter minus number to quit.")
while True:
    n = float(input("Please enter number of US gallons:\n"))
    if n < 0:
        print("Thank you for use. Goodbye!")
        break
    else:
        print(f"It is {exchange(n)} liters")