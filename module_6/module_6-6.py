def unit_price(diameter, price):
    return price / (3.14 * (0.5 * diameter) ** 2)


# main program
d1 = float(input("Please enter the diameter of first pizza:\n"))
p1 = float(input("Please enter the price of first pizza:\n"))
d2 = float(input("Please enter the diameter of second pizza:\n"))
p2 = float(input("Please enter the price of second pizza:\n"))
value_1 = unit_price(d1, p1)
value_2 = unit_price(d2, p2)
if value_1 > value_2:
    i = "The second pizza provides better value for money."
elif value_1 < value_2:
    i = "The first pizza provides better value for money."
else:
    i = "The two pizzas provide same value for monet."
print(i)