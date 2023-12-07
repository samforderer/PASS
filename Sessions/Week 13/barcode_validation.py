# AAA-PPP-CC 
# AAA — an integer from 111-999, 
# PPP — mix of letters and numbers, always 3 characters long CC - 
# CC — 2 digits integer from 00-99. 
# Dashes (-) are required.

correct_test_data = "123-A2B-55"
incorrect_test_data = "011-222-BB"
wrong_length = "123-A2B-5"
invalid_aaa = "B22-A2B-55"
invalid_ppp = "123-B#B-55"
invalid_cc = "123-A2B-BB"

# LENGTH CHECK 
def validate_barcode(code):
    if len(code) != 10:
        return False
    
    # dashes 
    if code[3] != "-" or code[7] != "-":
        return False
     
    # AAA
    
    aaa = code[:3]
    if aaa.isnumeric():
        if not 111 <= int(aaa) <= 999:
            return False
    else:
        return False
    
    # PPP
    if not code[4:7].isalnum():
        return False
    
    # CC 
    if not code[8:10].isdigit():
        return False
    
    return True

print(validate_barcode(correct_test_data))
print(validate_barcode(wrong_length))
print(validate_barcode(invalid_aaa))
print(validate_barcode(invalid_ppp))
print(validate_barcode(invalid_cc))
