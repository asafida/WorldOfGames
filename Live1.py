

def welcome(name):
    return (f"Hello {name} ""and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.\n"
            "Please choose a game to play: ")


def load_game(games):
    for i in games:
        print(i)
    try:
        choose = int(input())
        if choose == 1:
            print("You choose: ", games[0])
            diff = difficulty_level(1, 5)
            return diff
        elif choose == 2:
            print("You choose: ", games[1])
            diff = difficulty_level(1, 5)
            return diff
        elif choose == 3:
            print("You choose: ", games[2])
            diff = difficulty_level(1, 5)
            return diff
        else:
            print("you must choose number between 1-3:")
            load_game(games)
    except:
        print("you must choose number between 1-3:")
        load_game(games)


def difficulty_level(a, b):
    try:
        difficulty = int(input("Please choose game difficulty from 1 to 5:"))
        if difficulty in range(a, b + 1):
            print(difficulty)
            return difficulty
        else:
            print("you must choose number between 1-5:")
            difficulty_level(a, b)
    except:
        print("you must choose number between 1-5:")
        difficulty_level(a, b)


games = ["1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back",
         "2. Guess Game - guess a number and see if you chose like the computer",
         "3. Currency Roulette - try and guess the value of a random amount of USD in ILS"]
