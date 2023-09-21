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
lst_sort = sorted(lst, reverse= True)
for i in lst_sort[:5]:
    print(i)