import random

options = ("Rock", "Paper", "Scissor")
running = True
while running:
            computer = random.choice(options)
            player = None

            while player not in options:
                player = input("Enter Your choice:").capitalize()

            print(f"Player choice:{player}")
            print(f"computer choice:{computer}")

            if player == computer:
                print("It's a tie!")
            elif player == "Rock" and computer == "Scissor":
                print("You win!")
            elif player == "Paper" and computer == "Rock":
                print("You win!")
            elif player == "Scissor" and computer == "Paper":
                print("Your Win!")
            else:
                print("You lose!")
            again = input("Enter (Y/n) for play again or not:").lower()
            if again == "n":
                running = False

print("Thanks For playing")
