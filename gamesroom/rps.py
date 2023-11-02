import random as r

# user input 
user_choice = input("Enter rock, paper or scissors:")

computer_choice = r.randint(0,2)

# convert integer choice into "rock" "paper" or "scissors"

if computer_choice == 0:
    computer_choice = "rock"
elif computer_choice == 1:
    computer_choice = "paper"
else:
    computer_choice = "scissors"
    
print("computer choice " + computer_choice)