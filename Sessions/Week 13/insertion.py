def insert(list, index, value):
    inserted_list = list[:index] + [value] + list[index:] 
    return inserted_list


mylist = [1,3,5,7,9]

print(insert(mylist, 2, 10))
