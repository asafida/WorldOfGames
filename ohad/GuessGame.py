import random


def generate_number():
    try:
        difficulty = int(input("Please Enter Difficulty Number:"))
    except ValueError:
        difficulty = int(input("please enter integer: "))
    secret_number = random.uniform(1, difficulty)
    return secret_number, difficulty


def get_guess_from_user(diff):
    user_number = int(input("please choose number to guess between 1 to {}:".format(diff)))
    return user_number


def compare_results(num_gen, guess):
    if num_gen == guess:
        return True
    else:
        return False


def play():
    num_gen, diff = generate_number()
    guess = get_guess_from_user(diff)
    res = compare_results(num_gen, guess)
    return res


print(play())
