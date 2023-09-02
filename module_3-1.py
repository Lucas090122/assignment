length = float(input("What's the length of your zander in centimeters?\n"))
if length >= 42:
    print("You can take the zander.")
else: print(f"You have to release the fish back into the lake, the zander you caught is {42 - length} centimeters below the size limit.")