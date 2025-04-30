import random

def main():
    random_number = [random.randint(1, 100) for _ in range(10)] 
    print(*random_number)  

if __name__ == '__main__':
    main()    