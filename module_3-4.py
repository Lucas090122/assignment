year = int(input("Please enter year:\n"))
if year % 100 == 0:
    if year % 400 ==0:
        i = "This year is a leap year."
    else:
        i = "This year is not a leap year."
elif year % 4 ==0:
    i = "This year is a leap year."
else:
    i = "This year is not a leap year."
print(i)