import random as rd
random_list_1 = [rd.randint(0,9) for _ in range(3)]
#print(f"The 3-digit code is: {random_list_1}")

random_list_2 = [rd.randint(1,6) for _ in range(4)]
#print(f"The 4-digit code is: {random_list_2}")

three_digit = ''.join(map(str, random_list_1))
four_digit = ''.join(map(str, random_list_2))

print(f"The 3-digit code is: {three_digit}\nThe 4-digit code is: {four_digit}")
#print(map(str, random_list_1))