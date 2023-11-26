import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

player_move = input("Choose [r]ock, p[aper] or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissors
else:
    raise SystemExit("Invalid Input. Try again...")

bot_move = random.randint(1, 3)
if bot_move == 1:
    bot_move = rock
elif bot_move == 2:
    bot_move = paper
else:
    bot_move = scissors

print(f"The computer chose {bot_move}")

if player_move == rock and bot_move == scissors or \
        player_move == paper and bot_move == rock or \
        player_move == scissors and bot_move == paper:
    print("You win!")
elif player_move == bot_move:
    print("Draw!")
else:
    print("You lose!")
