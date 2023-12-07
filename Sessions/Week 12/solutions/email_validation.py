import string

email = input("enter email")

# break email into pieces 
    
def validate_email(email):
    
    if email.count('@') != 1:
        print("NO @")
        return False
    else:
        user_domain_split = email.split("@")
        print(user_domain_split)
        username = user_domain_split[0]
        domain = user_domain_split[1]
        
        # check username
        for i in username:
            if (not i.isalnum()) and (i != "."):
                print(f"{i} bad username")
                return False
           
        tld_start = 0 
        for i in range(len(domain) - 1, 0, -1):
            # find period
            if domain[i] == ".":
                tld_start = i
            
        local_domain = domain[:tld_start]
        tld = domain[tld_start + 1:]
        print(f"local: {local_domain}, tld: {tld}")
        
        # now check if domain part is alpha numeric
        for i in local_domain:
            if (not i.isalnum()) and (i != ".") and (i != "-"):
                print(f"{i} local domain")
                return False

        if (len(tld) != 3 and len(tld) != 2) or not tld.isalpha():
            print("bad tld")
            return False
    print("GOOD") 
    return True 

validate_email(email)