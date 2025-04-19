import math  # Import the math library so we can use the sqrt function

def main():
    # Get the two side lengths from the user and cast them to be numbers
    ab: float = float(input("\033[1;3mEnter the length of AB: "))
    ac: float = float(input("Enter the length of AC:"))

    # Calculate the hypotenuse using the two sides and print it out
    bc: float = math.sqrt(ab**2 + ac**2)
    print(f"\033[0mThe length of BC (the hypotenuse) is: {bc}")


if __name__ == '__main__':
    main()