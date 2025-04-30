

# Function to access an element
def access_element(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Index out of range."

# Function to modify an element
def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return lst
    except IndexError:
        return "Index out of range."

# Function to slice a list
def slice_list(lst, start, end):
    # No need for try-except; slicing in Python handles out-of-range gracefully
    return lst[start:end]

# Index Game function
def index_game():
    # Sample list
    
    lst = ['apple', 'banana', 'orange', 'grape', 'pineapple']
    print("Current list:", lst)

    print("\nChoose an operation: access, modify, slice")
    operation = input("Enter operation: ")

    if operation == "access":
        index = int(input("Enter index to access: "))
        result = access_element(lst, index)
        print("Result:", result)

    elif operation == "modify":
        index = int(input("Enter index to modify: "))
        new_value = input("Enter new value: ")
        result = modify_element(lst, index, new_value)
        print("Updated list:", result)

    elif operation == "slice":
        start = int(input("Enter start index: "))
        end = int(input("Enter end index: "))
        result = slice_list(lst, start, end)
        print("Sliced list:", result)

    else:
        print("Invalid operation.")

# Run the game
if __name__ == "__main__":
    index_game()
