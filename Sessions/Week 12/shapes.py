def validate_postal_code(code):
    # FIRST STEP -> LENGTH CHECK
    # IF BAD LENGTH, GET OUT 
    code = code.upper()
    if len(code) != 7 and len(code) != 6:
        print("INVALID LENGTH")
        return False
    
    # SECOND CHECK -> CORRECT FORM
    #A1A 1A1
    if len(code) == 7:
        # IF SPACE
        if \
        code[0].isalpha() and \
        code[1].isdigit() and \
        code[2].isalpha() and \
        code[3] == " " and \
        code[4].isdigit() and \
        code[5].isalpha() and \
        code[6].isdigit():
            return True

    elif len(code) == 6:
        # NO SPACE
        if \
        code[0].isalpha() and \
        code[1].isdigit() and \
        code[2].isalpha() and \
        code[3].isdigit() and \
        code[4].isalpha() and \
        code[5].isdigit():
            return True

    # IF FUNCTION MAKES HERE, IT IS BAD
    return False


print(validate_postal_code(input("enter postal code")))


