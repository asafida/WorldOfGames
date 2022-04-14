#def print_hi():
    # Python 3
    # txt = input("Type something to test this out: ")
    # Python 2
 #   txt = input("Type something to test this out: ")
  #  print("Is this what you just said? ", txt)


#if __name__ == '__main__':
    #print_hi()


def get_input():
    # Python 3
    # txt = input("Type something to test this out: ")
    # Python 2
    txt = input("Type something to test this out: ")
    return txt


def print_input(input):
  print("Is this what you just said? ", input)


if __name__ == '__main__':
    input = get_input()
    print_input(input)

