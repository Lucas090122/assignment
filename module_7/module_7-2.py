name_set = set()
while True:
    name = input("Please enter a name:\n")
    if name == "":
        print("End of name input.")
        break
    elif name in name_set:
        print("Existing name.")
    else:
        print("New name.")
        name_set.add(name)
print("The names recorded are:")
for name in name_set:
    print(name)