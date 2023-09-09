i = 0
right_acc = "python"
right_pass = "rules"
while True:
    i+=1
    acc = input("Please enter username:\n")
    pas = input("Please enter password:\n")
    if acc == right_acc and pas == right_pass:
        print("Welcome")
        break
    else:
        if i < 5:
            print("Incorrect username or password.")
        else:
            print("Access denied")
            break