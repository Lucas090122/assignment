lst = []
while True:
    num = input("Please enter number(empty string to quit):\n")
    if num == "":
        break
    try:
        num_1 = float(num)
        lst.append(num_1)
    except ValueError:
        print("Wrong input format, please enter a number.")
print(sorted(lst, reverse= True)[:5])