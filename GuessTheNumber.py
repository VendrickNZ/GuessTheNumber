import random
"""The computer generates a random number and the user tries to guess it."""


def random_number():
    """picks a random number from a range function and 
    returns the range bounds and chosen number"""
    range = number_range()
    low = range[0]
    high = range[1]
    return (random.randrange(low, high), low, high)


def number_range():
    """creates a range of numbers that the chosen number will lie within"""    
    low = random.randint(0, 20)
    high = random.randint(21, 50)
    return (low, high)


def guess_the_number():
    """The user attempts to guess the number chosen"""
    game_over = False
    number_and_range = random_number()
    chosen_number = number_and_range[0]
    low = number_and_range[1]
    high = number_and_range[2]
    chances = 3

    while game_over == False:
        guessed_number = int(input(f"Choose a number between {str(low)} and {str(high)}: "))
        if guessed_number < low or guessed_number > high:
            print(f"Number chosen not in range, try again")
        elif guessed_number == chosen_number and chances > 0:
            print(f"Congratulations {str(guessed_number)} was correct!")
            game_over = True
        elif chances <= 1:
            print(f"No chances remaining \nThe number was {chosen_number} \nGame Over")
            game_over = True
        else:
            chances -= 1
            print(f"Chances remaining: {chances}")
            if (chosen_number - low) and (high - chosen_number) >= 5: # whether it should decrease range
                low += (chosen_number - low) // 2 # decreases the range
                high -= (high - chosen_number) // 2

guess_the_number()
