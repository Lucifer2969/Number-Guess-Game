import random
from art import logo

number_list = []
for i in range(1,101):
    number_list.append(i)

def generate_number():
    """Generate the number that user needs to guess in the game."""
    return random.choice(number_list)
actual_number = generate_number()

def check_status(guess,actual):
    """Function to check user number is match for the computer generated number."""
    if guess > actual:
        return "Too High"
    elif guess < actual:
        return "Too Low"
    else:
        return f"You got it! The answer was {guess}"

def end_game():
    return 0

print(logo)
print("Welcome to the number Guessing Game.")
print("I am thinking a number between 1 to 100.")
mode = input("Choose the Difficulty mode. Type 'Easy' or 'Hard': ").lower()
if mode == 'easy':
    attempt = 10
elif mode == 'hard':
    attempt = 5
else:
    print("Wrong input Restart the game.")

while attempt > 0:
    print(f"You have {attempt} attempts to guess the number.")
    number_guess = int(input("Guess the number:- "))
    attempt -= 1
    result = check_status(number_guess,actual_number)
    if result == f"You got it! The answer was {number_guess}":
        attempt = end_game()
    print(result)

if result == "Too High" or result == "Too Low":
    print("You have exceeded your number of attempts.")