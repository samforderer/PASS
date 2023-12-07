password = input("Enter a password: ")

def validate_password(password):
    has_number = False
    has_upper = False
    has_lower = False 
    for i in password:
        if i.isnumeric():
            has_number = True
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True 
            
    return has_number and has_upper and has_lower

    
print(validate_password("Herl1l"))