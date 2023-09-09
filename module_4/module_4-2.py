while True:
    num = float(input("Please enter the inche:\n"))
    if num > 0:
        i = num * 30.48
        print(f"Transfer to centimeter is:\n{i}")
    else:
        print("Thank you for use.")
        break