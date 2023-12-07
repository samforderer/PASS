isNumeric = False

while not isNumeric:
    user_number = input("Enter a number: ")
    
    if user_number.isnumeric():
        isNumeric = True
    else:
        print("not a valid int")

print("thank you for the valid integer!")