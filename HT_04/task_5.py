# Create a Python program that repeatedly prompts the user for a number until a valid integer is provided.
# Use a try/except block to handle any ValueError exceptions, and keep asking for input until a valid integer is entered.
# Display the final valid integer.
from random import randrange

custom_range = int(input("Enter the range of nums you would like to guess "))
your_number = randrange(custom_range)
while True:
    print(f"Try to guess number in range you have choiced, i will remind you , your range was - {custom_range} ")
    try:
        guess_num = int(input("Enter your choice "))
        if guess_num == your_number:
            print(f"It was right number , your win number was {your_number}")
            break
        else:
            print("Wrong guess. Try again!")
    except ValueError:
        print(f"It was not int , lets play by rules")
