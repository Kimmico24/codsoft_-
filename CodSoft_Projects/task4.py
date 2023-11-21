import random

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Scissors" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Rock"):
        return "You win!"
    else:
        return "You lose!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").capitalize()
        if user_choice not in ["Rock", "Paper", "Scissors"]:
            print("Invalid choice, please try again.")
            continue

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score - You: {user_score}, Computer: {computer_score}")

        if input("Play again? (yes/no): ").lower() != "yes":
            break

if __name__ == "__main__":
    main()
