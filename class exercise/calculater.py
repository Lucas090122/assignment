def add(a, b):
    return a + b

def sbtr(a, b):
    return a - b

def mlti(a, b):
    return a * b

def divd(a, b):
    return a / b

while True:
    while True:
        user_choice = str(input("1. Addition 2. Subtraction 3. Multiplication 4. Division\nPlease choose the function you need(1/2/3/4/(for finish: stop)):\n"))
#        if user_choice == "1" or user_choice == "2" or user_choice == "3" or user_choice == "4" or user_choice == "stop":
        if user_choice in ("1", "2", "3", "4", "stop"):
            break
        else:
            print("Error: Wrong Function Code.")
    if user_choice == "stop":
        break
    num_1 = float(input("Please enter the first number:"))
    num_2 = float(input("Please enter the second number:"))
    if user_choice == "1":
        i = add(num_1, num_2)
    elif user_choice == "2":
        i = sbtr(num_1, num_2)
    elif user_choice == "3":
        i = mlti(num_1, num_2)
    elif user_choice == "4":
        if num_2 == 0:
            i = "The divisor cannot be 0."
        else:
            i = divd(num_1, num_2)
    print(i)
print("Thank you for use.")