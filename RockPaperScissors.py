import random
user_score = 0
computer_score = 0
while True:
    print("\n===== ROCK PAPER SCISSORS =====")
    print("Choose one:")
    print("1. Rock")
    print("2. Paper")  
    print("3. Scissors")
    choice = input("Enter your choice (rock/paper/scissors): ")
    choice = choice.lower() 
    if choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice! Please try again.")
        continue
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"\nYou chose: {choice}")
    print(f"Computer chose: {computer_choice}")
    if choice == computer_choice:
        print("It's a Tie!")
    elif ((choice == "rock" and computer_choice == "scissors") or(choice == "paper" and computer_choice == "rock") or(choice == "scissors" and computer_choice == "paper")):
        print("You Win!")
        user_score += 1
    else:
        print("Computer Wins!")
        computer_score += 1
    print("\n===== SCORE =====")
    print(f"You: {user_score}")
    print(f"Computer: {computer_score}")
    play_again = input("\nDo you want to play again? (yes/no): ")
    play_again = play_again.lower()
    if play_again != "yes":
        print("\nGame over!")
        break