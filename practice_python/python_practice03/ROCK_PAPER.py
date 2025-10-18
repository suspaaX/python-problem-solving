import random

from click import option

user_wins = 0
computer_wins = 0

option = ["rock" , "paper","scissors"]

while True:
    user_input = input("Type Rock/paper/scissors or Q to quit.").lower()
    if user_input == "q": 
       break
    
    if user_input not in ["rock","paper","scissors"]:
        continue

    random_number = random.randint(0,2)  
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("computer picked",computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissiors" 
    print("You won!")
    user_wins += 1 
    continue

    
    if user_input == "rock" and computer_pick == "scissiors" 
    print("You won!") 
    user_wins += 1
    continue

 
    if user_input == "rock" and computer_pick == "scissiors" 
    print("You won!")
    user_wins += 1
    continue

    else:
        print("You lost!")
        computer_wins += 1


print("You won", )
print("Goodbye!") 