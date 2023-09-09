def sum(a, b):
    return a + b


list_1 = []
list_2 = []
ans = 0
while True:
    if ans == "no":
        break
    num_1 = int(input("Please enter first number:"))
    num_2 = int(input("Please enter second number:"))
    list_1.append((num_1, num_2))
    list_2.append(num_1)
    list_2.append(num_2)
    ans = str(input("Do you wanna continue? Please enter (anything/no)"))
print(f"The numbers you've provided are {list_2}")
for i in list_1:
    total = sum(i[0], i[1])
    print(f"The sum of {i[0]} and {i[1]} is {total}")
