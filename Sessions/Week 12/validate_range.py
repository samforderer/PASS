# function that takes arguments min, max and value 
# determines if value is in range return boolean

def check_if_in_range(min, max, value):
    if (min <= value <= max):
        return True
    else:
        return False

# check if outside range
def check_if_outside_range(min, max, value):
    if (value <= min or value >= max):
        return True
    else:
        return False
        

# DECLARE VARIABLES (INPUT)
my_number = 4500 
min = 3000
max = 5000

# RUN FUNCTIONS (PROCESSING)
is_my_number_in_range = check_if_in_range(5, 2000, my_number)
is_my_number_outside_range = check_if_outside_range(min, max, my_number)

# VIEW (OUTPUT)
print(f"min = {min}, max = {max}, value = {my_number}, is outside range = {is_my_number_outside_range}")
print(is_my_number_in_range)

