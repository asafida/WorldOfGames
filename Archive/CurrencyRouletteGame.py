import requests
import random
import time
import os

# Where USD is the base currency you want to use
url = 'https://v6.exchangerate-api.com/v6/19abb2dd64cc30bc634b944a/pair/USD/ILS'


# Making our request
response = requests.get(url)
data = response.json()
c = (data["conversion_rate"])


generate = random.randint(1,101)
#print(generate)

def get_money_interval(choose_dif):
    d = choose_dif
    t = int(generate*c)
    money_interval = (t - (5 - d), t +(5 - d))
    return money_interval


def get_guess_from_user(generate):
    guess = int(input("Try to guess the ILS value of {} USD:".format(generate)))
    return guess


def c_play(choose_dif):
   interval = get_money_interval(choose_dif)
   guess =   get_guess_from_user(generate)
   if guess in range((interval[0]),(interval[1])):
       print("You Win!")
   else:
       print("You Lose!")


#get_money_interval()
#get_guess_from_user(generate)

