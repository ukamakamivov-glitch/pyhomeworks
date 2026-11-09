import random

text = ['rock', 'paper', 'scissors']

player_score = 0
computer_score = 0

while player_score < 5 and computer_score < 5 :

    player = input("Rock, paper, or scissors : ").lower()

    computer = random.choice(text)

    if player not in text:
        print("Invalid choice!")
        continue
    if player == computer:
        print("Draw!")
        continue
    elif (player == 'rock' and computer == 'scissors') or (player == 'scissors' and computer == 'paper') or (player == 'paper' and computer == 'rock') :
        player_score += 1
        print("Player wins this round!")
    else:
        computer_score += 1
        print("Computer wins this round!")
else:
    if player_score == 5:
        print("You win!")
    else:
        print("Computer wins!")

print("Player ballari :",player_score, "Kompyuter tuplagan ballari :",computer_score)