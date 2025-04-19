def main():
    # Get the numbers we want to divide
    dividend: int = int(input("\033[1;3m Please enter an integer to be divided: "))
    divisor: int = int(input("Please enter an integer to divide by: "))

    quotient: int = dividend // divisor  # Divide with no remainder/decimals (integer division)
    remainder: int = dividend % divisor  # Get the remainder of the division (modulo)
    
    print(f"\033[0mThe result of this division is {quotient} with a remainder of {remainder}")


# There is no need to edit code beyond this point

if __name__ == '__main__':
    main()
