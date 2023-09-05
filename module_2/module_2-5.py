print("Please enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).")
talent = float(input("Enter talents: "))
pound = float(input("Enter pounds: "))
lot = float(input("Enter lots:"))
sum = talent * 20 * 32 * 13.3 + pound * 32 * 13.3 + lot * 13.3
kg = int(sum / 1000)
g = round(sum - kg * 1000, 2)
print(f"The weight in modern units:\n{kg} kilograms and {g} grams.")