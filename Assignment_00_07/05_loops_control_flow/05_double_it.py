def main():
    cur_value = int(input("Enter a number: "))

    while cur_value < 100:
        cur_value = cur_value * 2
        print(cur_value, end=" ")
if __name__ == '__main__':
    main()