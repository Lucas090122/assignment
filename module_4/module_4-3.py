list_1 = []
while True:
    num = input("Please enter a number(enter an empty string to quit):\n")
    if num == "":
        break
    try:
        num = float(num)
        list_1.append(num)
    except ValueError:
        print("Wrong input format, please enter a number.")
if list_1 == []:
    print("You haven't enter any number.")
else:
    i = max(list_1)
    j = min(list_1)
    print(f"The smallest number is {j}\nThe largest number is {i}")