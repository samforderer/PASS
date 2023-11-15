import check_prime as cp

# This file imports the check_prime file that is stored in the same directory. 
# You must download that file and store it in same directory for this to run 
# as expected. 


# lists all prime from 2 to the specified limit
def list_all_primes(limit):
    prime_list = []
    
    for i in range(2, limit + 1):
        if cp.check_prime(i):
            prime_list.append(i)
    
    return prime_list

# Test function
print(list_all_primes(51))
