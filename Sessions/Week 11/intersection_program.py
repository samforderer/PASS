# Functions 

# loop until user enters exit, add all inputs to a list, return the list
def create_list_from_user_input():
    
    list = []
    
    user_input_item = input("Enter item for list or enter 'exit' to stop: ")

    while user_input_item != "exit": 
        list.append(user_input_item)
        user_input_item = input("Enter item for list or enter 'exit' to stop: ")
    
    return list


# declare the lists 

common_values_list = []

# CREATE LIST A 
print("ENTERING LIST A")
listA = create_list_from_user_input() 
 
# CREATE LIST B   
print("ENTERING LIST B")
listB = create_list_from_user_input()


# PROCESSING 
# Loop through listA 
# inside that loop, loop through listB 
# check if the items are equal 
# if so, add them to common_values_list 

for itemA in listA:
    for itemB in listB:
        print("Current common values: ", common_values_list)
        if (itemA == itemB) and (itemA not in common_values_list):
            common_values_list.append(itemA)
            
print(common_values_list)