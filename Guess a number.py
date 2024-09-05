import random
def guess_number(x):
    random_number = random.randint(1, x)
    guess = 0
    number_of_guesses = 0
    number_of_attempts = 5
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}:"))
        number_of_guesses += 1
        if number_of_guesses >5:
            print("sorry! better luck next time")
            break
        if guess > random_number:
            print("Hey your guess is incorrect please guess too low")
            number_of_attempts -= 1
            print(f"you have only {number_of_attempts} more attempts")
        elif guess < random_number:
            print("Hey your guess is incorrect please guess too high")
            number_of_attempts -= 1
            print(f"you have only {number_of_attempts} more attempts")
        else:
            print(f"Hey you got it gem! you have used '{number_of_guesses}' guess attempts to catch it! ")

guess_number(10)
        
