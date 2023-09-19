# Create a dictionary called "doctor"
doctor = {
    'Title': 'Jr',
    'Name': 'Smith',
    'Employment_year': '1840'
}

# Print the dictionary
print(doctor)

# Add new key-value (gender)
doctor['Gender'] = 'male'

# function
def doctor_details(title):
    if doctor['Title'] == title:
        result = f"Title: {doctor['Title']} Name: {doctor['Name']} Year: {doctor['Employment_year']} Gender: {doctor['Gender']}"
    else:
        result = "No related title in doctor"
    return result

# Test function
title = input("What's the title you wanna check?\n")
i = doctor_details(title)
print(i)