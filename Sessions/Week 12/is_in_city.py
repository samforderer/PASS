# City and country

city_and_code = [["HAMILTON", 905], ["TORONTO", 416]]

value = "(905) 555-2953"
# check if area code is in the array 



# is area code in list 
def validate_area_code(array, phone_number):
    area_code = phone_number[1:4]

    for city in array: 
        print(f"area code = {area_code}, array value = {city[1]}")
        if area_code == str(city[1]):
            return True
    
    return False 
is_valid = validate_area_code(city_and_code, value)
print(is_valid)

