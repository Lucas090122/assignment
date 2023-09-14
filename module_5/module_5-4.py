print("Please provide 5 names of cities.")
i = 0
lst = []
for i in range(5):
    city = input("Please enter a city name:")
    lst.append(city)
    i += 1
print("The cities you chose are:")
for city in lst:
    print(city)