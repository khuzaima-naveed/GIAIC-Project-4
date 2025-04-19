def main():
    lst = []  # Make an empty list to store things in

    BLUE = '\033[94m'  # ANSI code for blue text
    RESET = '\033[0m'  # Resets text color to default

    val = input(f"{BLUE}Enter a value: ")  # Get an initial value
    while val:  # While the user input isn't an empty value
        lst.append(val)  # Add val to list
        val = input(f"{BLUE}Enter a value: ")  # Get the next value to add

    # print("Here's the list:", lst)
    print(f"{RESET}Here's the list: {lst}")  # Print the list with reset color


if __name__ == '__main__':
    main()
