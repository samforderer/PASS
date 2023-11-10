# Checks if a number is prime. Returns True if it is, False if not. 
def check_prime(number): 
    
    if number <= 1:
        return False    
        
    elif number == 2:
        return True 

    else:
        for i in range(3, number):
            if number % i == 0: 
                return False
    # if it makes it to the end 
    return True


# Test function
print(check_prime(9))
