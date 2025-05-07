import random

def main():
    print("🗻 Rock, 📄 Paper, ✂️ Scissors - Let's play!")

    options = ["rock", "paper", "scissors"]
    user_choice = input("Choose rock, paper, or scissors: ").lower()

    if user_choice not in options:
        print("Invalid choice. Please choose rock, paper, or scissor.")
        return

    computer_choice = random.choice(options)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("🎉 You win!")
    else:
        print("😢 You lose!")

if __name__ == "__main__":
    main()
