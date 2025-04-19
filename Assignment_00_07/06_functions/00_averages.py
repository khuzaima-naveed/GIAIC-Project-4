def average(a: float, b: float):
    """
    Returns the number which is half way between a and b
    """
    sum = a + b
    return sum / 2

def main():
    avg_1 = average(0, 10)
    avg_2 = average(8, 10)
    
    final = average(avg_1, avg_2)
    print("Average of first value is", avg_1)
    print("Average of first value is", avg_2)
    print("The sum of both averages is", final)
    

if __name__ == '__main__':
    main()