
def add_score(choose_dif):
    my_score = open("Score.txt", "r+")
    for score in my_score.read():
        my_score.truncate(0)
        current_score = int(score) + (choose_dif*3) + 5
        print(current_score)
        my_score = open("Score.txt", "r+")
        my_score.write(f"{current_score}")
        for score in my_score.readlines():
            print(score)
        #my_score.close()


def show_names():
    my_file = open("Score.txt")
    for name in my_file.readlines():
        score = int(name)
        print(score)
        current_score = score + 5
        print(current_score)

add_score(5)

#with open("score.txt") as my_score:
   # for line in my_score.readlines():
    #    print(line)


