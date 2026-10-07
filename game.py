import random

computer_score = 0
my_score = 0

game_choice = ["rock", "paper", "scissor",]
print("welcome to our mini RSP game!!!")

while True:
    my_choice = input("put in your choice in this list" + str(choices))
    computer_choice = random.choices(game_choices)
    
    if my_choice == "rock" and computer_choice == "paper":
        print("computer wins, you lost")
        computer_score = computer_score + 1
    elif my_choice == "paper" and computer_choice == "rock":
        print("you won, computer lost")
        my_score = my_score + 1
    elif my_choice == "scissors" and computer_choice == "rock":
        print("computer wins, you lost")
        computer_score = computer_score + 1
    elif my_choice == "rock" and computer_choice == "scisssor":
        print("you wins, computer lost")
        my_score = my_score + 1
    elif my_choice == "paper" and computer_choice == "scissor":
        print("computer wins, you lost")
        computer_score = computer_score + 1
    elif my_choice == "scissor" and computer_choice == "paper":
        print("you wins, computer lost")
        my_score= my_score + 1
        
    else:
        print("it's a tie")
        
        
        
    print("my score:" + )