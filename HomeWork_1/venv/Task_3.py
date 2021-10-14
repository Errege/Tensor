import random
from random import Random


def numbers():
    less = 0
    more = 100

    number = random.randint(less, more)
    while True:
        print(number)
        answer = input()

        if answer == "Верно":
            break
        elif answer == "Больше":
            less = number + 1
            number = random.randint(less, more)
            continue
        elif answer == "Меньше":
            more = number - 1
            number = random.randint(less, more)
            continue
        else:
            print("Введите команду: Больше или Меньше")
            continue


numbers()
