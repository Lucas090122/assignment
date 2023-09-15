def cut_list(given_list):
    for i in given_list:
        if i % 2 != 0:
            given_list.remove(i)
    return given_list


# main program
print("Enter integer to create a list, any other to finish")
example_list = []
while True:
    num = input()
    if num.isdigit():
        example_list.append(int(num))
    else:
        print("Finish create the list")
        break
print(f"The example list is:\n{example_list}")
new_list = cut_list(example_list)
print(f"The cut down list is:\n{new_list}")