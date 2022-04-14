import random
import time
import os


def generate_sequence(choose_dif):
    generate = random.sample(range(1,101),choose_dif)
    print(sorted(generate))
    time.sleep(0.7)
    os.system('clear')
    return sorted(generate)


def get_list_from_user(choose_dif):
    user_lst = []
    # iterating till the range
    print("please enter a list of {} numbers between 1-100 :".format(choose_dif))
    while len(user_lst) < choose_dif:
     ele = int(input())
     if  1 <= ele <= 100:
         user_lst.append(ele)  # adding the element
     else:
            print("must be a number between 1-100")

    return sorted(user_lst)


def equal(gen,user):
    if gen == user :
       return True
    else:
       return False

def m_play(choose_dif):
    gen = generate_sequence(choose_dif)
    user = get_list_from_user(choose_dif)
    if equal(gen, user) == True:
        print("You Win!")
    else:
        print("You Lose!")



