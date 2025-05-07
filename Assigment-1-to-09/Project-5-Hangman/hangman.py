import random
import string
from word_list import word_list
def main():
    # List of words to choose from
   
    chosen_word = random.choice(word_list)
    guessed_letters = []
    tries = 6

    print("🎮 Welcome to Hangman!")
    print("You have", tries, "tries to guess the word.")

    # Game loop
    while tries > 0:
        display_word = ""
        for letter in chosen_word:
            if letter in guessed_letters:
                display_word += letter
            else:
                display_word += "_"

        print("\nWord:", " ".join(display_word))

        if "_" not in display_word:
            print("🎉 Congratulations! You guessed the word:", chosen_word)
            break

        guess = input("Guess a letter: ").lower()

        # Validate input
        if len(guess) != 1 or guess not in string.ascii_lowercase:
            print("❗ Please enter a single alphabet letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ You already guessed that letter.")
        elif guess in chosen_word:
            guessed_letters.append(guess)
            print("✅ Good guess!")
        else:
            guessed_letters.append(guess)
            tries -= 1
            print("❌ Wrong guess! Tries left:", tries)

    else:
        print("💀 You lost! The word was:", chosen_word)

if __name__ == "__main__":
    main()
