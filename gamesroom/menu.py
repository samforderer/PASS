import multi_game

# print out options
def print_menu():
    # multiplication game
    print("1. multiplication game")
    print("2. option 2")
    print("3. option 3")

while True:
    print_menu() 
    choice = input("Enter choice: ")
    
    if choice == "1":
        multi_game.game()
    elif choice == "2":
        print("option 2")
    elif choice == "3":
        print("option 3")
    elif choice == "exit":
        break
    else:
        print("invalid")


