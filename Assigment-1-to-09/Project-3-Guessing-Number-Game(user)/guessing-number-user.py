import random

def main():
    print("🔢 Think of a number between 1 and 100 and I will try to guess it!")
    input("Press Enter when you're ready...")

    low = 1
    high = 100
    attempts = 0
    guessed = False

    while not guessed:
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # only one option left
        attempts += 1

        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").strip().upper()

        if feedback == "H":
            high = guess - 1
        elif feedback == "L":
            low = guess + 1
        elif feedback == "C":
            guessed = True
            print(f"🎉 I guessed it in {attempts} tries!")
        else:
            print("Please enter H, L, or C.")

if __name__ == "__main__":
    main()
