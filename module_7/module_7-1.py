seasons = ("Spring", "Summer", "Autumn", "Winter")
number = input("Please enter a number for month(1~12):\n")
if number.isdigit():
    number = int(number)
    if number in [12, 1, 2]:
        i = seasons[3]
    elif number in [3, 4, 5]:
        i = seasons[0]
    elif number in [6, 7, 8]:
        i = seasons[1]
    elif number in [9, 10, 11]:
        i = seasons[2]
    else:
        i = "not a month number, please enter number between 1 & 12"
    print(f"The month number {number} is {i}.")
else:
    print("Wrong code! Please enter number between 1 & 12.")