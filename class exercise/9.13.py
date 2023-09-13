# lst = []
# print("Options\n1. Add a task\n2. Remove a task\n3. Display tasks\n4. Quit")
# while True:
#     i = input("Enter your choice(1/2/3/4):")
#     if i == "1":
#         item = input("Add a task:")
#         lst.append(item)
#     elif i == "2":
#         item_1 = input("Remove a task:")
#         if item_1 in lst:
#             print(f"Task {item_1} removed")
#             lst.remove(item_1)
#         else:
#             print(f"Task {item_1} is not in the list")
#     elif i == "3":
#         print(f"All tasks are {lst}")
#     elif i == "4":
#         print("Goodbye!")
#         break
#     else:
#         print("Wrong code!")
shopping_dict = {'milk': 2, 'juice': 3, 'oat': 4}
def add(item, n):
    shopping_dict[item] = n
def remove(item):
    shopping_dict.pop(item)
print("options:\n1. add on item\n2. remove item\n3. show your list\n4. quit")
while True:
    choice = input("Enter your choice(1/2/3/4):")
    if choice == "1":
        item = input("What you wanna add to list?\n")
        n = int(input("How many you need?\n"))
        i = add(item, n)
    elif choice == "2":
        item = input("What you wanna remove from list?\n")
        i = remove(item)
    elif choice == "3":
        print(shopping_dict)
    elif choice == "4":
        break
    else:
        print("Wrong code!")