# Python function that takes a list of integers as input and returns the sum of all the even numbers in the list.


def sum_even_list(list):
    
    sum_even = 0
    
    for i in list:
        if i % 2 == 0:
            sum_even += i
    
    return sum_even
        

    
# Create sample list
my_list = [1, 2, 3, 4, 5]

print(sum_even_list(my_list))

