SENTENCE_START: str = "Panaversity is fun. I learned to program and used Python to make my " # adjective noun verb

def main():
        
        RESET = '\033[0m'
    # Get the three inputs from the user to make the adlib
        adjective: str = input("\033[1;3mPlease type an adjective and press enter. ")
        noun: str = input("Please type a noun and press enter. ")
        # verb: str = input("Please type a verb and press enter.")
        verb =input(f"Please type a verb and press enter.")

    # Join the inputs together with the sentence starter
        print(f"{RESET}{SENTENCE_START}{adjective} {noun} {verb}!")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()