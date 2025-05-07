import random

print("Welcome to the Password Generator ✨")

chars ='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+,.<>?' 
number = int(input("How many passwords do you want to generate? "))
length = int(input("Your password length? "))

print('\nHere are your passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)