# create a module 
def validate_password(password):
    # flags 
    has_upper = False
    has_lower = False
    has_digit = False
    
    # loop through each character 
    if len(password) < 10:
        return False 
    elif not password.isalnum():
        return False    
   
    # congratulations, you made it to the loop 
    for i in password:
        if i.isupper():
            has_upper = True
        if i.islower():
            has_lower = True 
        if i.isdigit():
            has_digit = True  

    if has_upper and has_lower and has_digit:
        return True 
    else:
        return False
    
#True Test case    
print(validate_password("Password123"))

#false Test case
print(validate_password("password123"))
