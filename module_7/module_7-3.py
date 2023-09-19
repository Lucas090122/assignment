print("Options:")
print("1. Add a new airport")
print("2. Fetch airport")
print("3. Quit")
airport_dic = {}
while True:
    user_choice = input("Please enter your choice(1/2/3):")
    if user_choice == "1":
        icao_code = input("Please enter the ICAO code of airport:\n")
        if icao_code in airport_dic:
            print("This airport is already in the record.")
        else:
            airport_name = input("Please enter the airport name:\n")
            airport_dic[icao_code] = airport_name
            print("New record added.")
    elif user_choice == "2":
        target_icao = input("Please enter the ICAO code of the airport:\n")
        if target_icao in airport_dic:
            print(f"The corresponding airport name for code {target_icao} is: {airport_dic[target_icao]}.")
        else:
            print("No recorded ICAO code.")
    elif user_choice == "3":
        print("Thank you for using. Goodbye!")
        break
    else:
        print("Wrong option code, please choose from 1/2/3")