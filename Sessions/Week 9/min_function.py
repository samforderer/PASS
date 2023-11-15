def my_min(list):
    lowest = list[0]
    for i in list:
        if i < lowest:
            lowest = i 
    
    return lowest 

def my_max(list):
    highest = list[0]
    for i in list:
        if i > highest:
            highest = i 
    
    return highest 

numbers = [50, 100, 200, 2]

print(f"The lowest is: {my_min(numbers)}")
print(f"The highest is: {my_max(numbers)}")