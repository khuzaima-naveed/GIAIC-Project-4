def add_many_numbers(numbers)-> int:
   
    total: int = 0
    for number in numbers:
        total += number

    return total


def main():
    numbers: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()