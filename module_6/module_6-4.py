def sum_of_list(target_list):
    return sum(target_list)


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
list_sum = sum_of_list(example_list)
print(f"The sum of this list is {list_sum}")