import random


def generate_number(choose_dif):
    secret_number = int(random.uniform(1, choose_dif))
    return secret_number


def get_guess_from_user(choose_dif):
    user_number = int(input("please choose number between 1 to {}:".format(choose_dif)))
    return user_number


def compare_result(gen, user_g):
    if gen == user_g:
        return True
    else:
        return False


def g_play(choose_dif):
    gen = generate_number(choose_dif)
    user_g = get_guess_from_user(choose_dif)
    if compare_result(gen, user_g) == True:
        print("You Win!")
    else:
        print("You Lose!")


