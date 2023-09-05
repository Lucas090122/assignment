gender = input("Please enter gender:\n")
g_i = float(input("Please enter hemoglobin value (g/l):\n"))
if gender == "male":
    if g_i < 134:
        i = "Your hemoglobin value is low."
    elif g_i > 167:
        i = "Your hemoglobin value is high."
    else:
        i = "Your hemoglobin value is normal."
elif gender == "female":
    if g_i < 117:
        i = "Your hemoglobin value is low."
    elif g_i > 155:
        i = "Your hemoglobin value is high."
    else:
        i = "Your hemoglobin value is normal."
else:
    i = "Enter error."
print(i)