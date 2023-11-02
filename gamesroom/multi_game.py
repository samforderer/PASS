import random as r 

def game():
    score = 0

    for i in range(3):
        x = r.randint(1,10)
        y = r.randint(1,10)
        
        answer = x * y
        print(f"{x} X {y} = ?")
        user_answer = int(input("Enter your answer: ")) #prints on same line
        
        if answer == user_answer:
            print("Correct!")
            score += 10
        else:
            score -= 5
        
    print(f"YOUR SCORE WAS {score}")
