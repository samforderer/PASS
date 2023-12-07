# asks the user to enter a list of integers, 
# one at a time, until they enter the value 0. 

# declare list 
list = []

while True:
    
    number = int(input("enter number: "))
    
    if number == 0:
        break
    else:
        list.append(number) 
        
# compute print sum of all positive integers and product of all negative
sum_positive = 0 
product_negative = 1

for i in list:
    if i > 0:
        sum_positive += i 
    elif i < 0:
        product_negative *= i
        
print(f"sum of positives: {sum_positive}, product of negative: {product_negative}")
print("Thank you for joining")