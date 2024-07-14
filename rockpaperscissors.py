player_wins=0
computer_wins=0

import random

while player_wins < 2 and computer_wins < 2:
    choices = ["rock" , "paper" , "scissors"]

    print("Lets's play Rock, Paper, Scissors!!!")

    player_choice=input ("Choose your move: Rock, Paper or Scissors" ).lower()
    computer_choice=random.choice(choices)

    print(f"Computer chose: {computer_choice}")
    print(f"Player chose: {player_choice}")

    if (player_choice == "rock" and computer_choice == "paper") or (player_choice == "rock" and computer_choice == "scissors") or (player_choice == "scissors" and computer_choice == "paper"):
        winner = "Player"
        player_wins+=1

    elif (player_choice == "rock" and computer_choice == "rock") or (player_choice == "scissors" and computer_choice == "scissors") or (player_choice == "paper" and computer_choice == "paper"):
        winner = "Tie"
    
    else:
        winner = "Computer"
        computer_wins+=1


    if winner == "Player":
        print("Player wins")

    elif winner == "Computer":
        print("Computer won")

    else:
        print("It's a tie")


print(f"WIN Count: Player ({player_wins}) || Computer ({computer_wins})")

if player_wins > computer_wins:
    print("PLAYER WON!!")
else:
    print("Computer won :(")

print("Hope you enjoyed the game!! Lets's play again another time <3")   





    

