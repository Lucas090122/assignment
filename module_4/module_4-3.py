list_1 = []
while True:
    num = input("Please enter a number(enter an empty string to quit):\n")
    if num == "":
        break
    num = float(num)
    list_1.append(num)
i = max(list_1)
j = min(list_1)
print(f"The smallest number is {j}\nThe largest number is {i}")