def miles_to_kilometers(miles):
    kilometers = miles * 1.60934
    return kilometers

def kilometers_to_miles(kilometers):
    miles = kilometers / 1.60934
    return miles

# Prompt the user to choose the conversion direction
print("Choose a conversion direction:")
print("1. Miles to Kilometers")
print("2. Kilometers to Miles")
choice = input("Your choice (1 or 2): ")

# Prompt the user to enter the value to be converted
value = float(input("Enter the value to be converted: "))

# Perform the conversion based on the user's choice
if choice == "1":
    result = miles_to_kilometers(value)
    print("{} miles is equal to {} kilometers.".format(value, result))
elif choice == "2":
    result = kilometers_to_miles(value)
    print("{} kilometers is equal to {} miles.".format(value, result))
else:
    print("Invalid choice.")
