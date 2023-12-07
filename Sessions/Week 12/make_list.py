# take a limit from user
# input all number from 1 to the input 
# into a list 
# return list 

def make_list(maximum):
    # initialize a list 
    list = []
    for i in range(1, maximum + 1):
        list.append(i)

    return list

print(make_list(int(input("Enter Maximum: "))))

