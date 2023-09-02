c_class = input("Please enter your cabin class of the cruise ship:\n")
if c_class == "LUX":
    i = "It's upper-deck cabin with a balcony."
elif c_class == "A":
    i = "It's above the car deck, equipped with a window."
elif c_class == 'B':
    i = "It's windowless cabin above the car deck."
elif c_class == "C":
    i = "It's windowless cabin below the car deck."
else:
    i = "Error: Invalid cabin class."
print(i)