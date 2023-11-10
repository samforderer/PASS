import random as r

# declare variables
userChoice = ""
roundNumber = 0 
score = 0

# start round

while roundNumber < 3:
    
    # user input 
    choices = ["rock", "paper", "scissors"]
    
    computer_choice = choices[r.randint(0,2)]
    userChoice = input("Enter rock, paper or scissors: ") 
    # user input validation
    while not userChoice in choices:
        userChoice = input("Enter rock, paper or scissors: ")

    # Provide feedback to user of what everyone chose  
    print(f"User chooses: {userChoice}, Computer chooses: {computer_choice}")

    # ties
    if userChoice == computer_choice:
        print ("Tie")
        continue
    elif (userChoice == "rock" and computer_choice == "scissors") or \
    (userChoice == "paper" and computer_choice == "rock") or \
    (userChoice == "scissors" and computer_choice == "paper"):
        print("user wins round")
        score += 1
    else:
        print("Computer wins round")
        
    roundNumber += 1
    
if score == 2:
    print("USER WINS THE GAME")
else:
    print("COMPUTER WINS THE GAME")