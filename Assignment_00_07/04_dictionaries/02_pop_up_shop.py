def main():
    fruits = {'apple': 3, 'grapes': 50, 'pear': 80, 'kiwi': 1, 'orange': 2, 'mango': 5}
    
    total_cost = 0
    for fruit_name in fruits:
        price = fruits[fruit_name]
        amount_bought = int(input("How many (" + fruit_name + ") do you want to buy?: "))
        total_cost += (price * amount_bought)
    
    print("Your total is PKR" + str(total_cost))



if __name__ == '__main__':
    main()