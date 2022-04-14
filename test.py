def welcome(name):
    return (f"Hello {name} ""and welcome to the World of Games (WoG).\n"
            "Here you can find many cool games to play.\n"
            "Please choose a game to play: ")


def load_game():
    # checking input
    try:
        choose = int(
            input("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                  "2. Guess Game - guess a number and see if you chose like the computer\n"
                  "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"))
    except ValueError:
        choose = int(input("please enter integer: "))
    # while loop until choose is in range
    while 1 <= choose <= 3:
        if choose == 1:
            print(
                "You choose: 1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it "
                "back")
            difficulty_level()
        elif choose == 2:
            print("You choose: 2. Guess Game - guess a number and see if you chose like the computer")
            difficulty_level()
        elif choose == 3:
            print("You choose: 3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
            difficulty_level()
    else:
        try:
            choose = int(input("you must choose number between 1-3: "))
            return choose
        except ValueError:
            choose = int(input("please enter integer: "))
            return choose


# helper function
def difficulty_level():
    # checking input
    try:
        difficulty = int(input("Please choose game difficulty from 1 to 5: "))
    except ValueError:
        difficulty = int(input("please enter integer: "))
    # while loop until difficulty is in range
    while True:
        if 1 <= difficulty <= 5:
            print(difficulty)
            break
        else:
            try:
                difficulty = int(input("you must choose number between 1-5: "))
            except ValueError:
                difficulty = int(input("please enter integer: "))
