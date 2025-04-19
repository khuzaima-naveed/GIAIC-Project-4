def main():
    def in_range(n, low, high):
        """
        Returns True if n is between low and high, inclusive. 
        high is guaranteed to be greater than low.
        """
        if n >= low and n <= high:
            return True
        return False

    # Get input from user
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Call the function and print the result
    result = in_range(n, low, high)
    print("Is in range?", result)

if __name__ == '__main__':
    main()
