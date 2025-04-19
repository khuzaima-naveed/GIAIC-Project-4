def print_multiple(message, repeat):
    for i in range(repeat):
        print(message)

def main():
    # ANSI escape code for blue text
    BLUE = '\033[94m'
    RESET = '\033[0m'

    # Make prompt blue, user input stays default color
    message = input(f"{BLUE}Please type a message: {RESET}")
    repeat = int(input(f"{BLUE}Enter a number of times to repeat your message: {RESET}"))

    print_multiple(message, repeat)

if __name__ == "__main__":
    main()
