def append_word_to_age():
    number = input("Введите целое число в диапазоне от 0 до 200: ")

    if int(number) % 5 == 0 or int(number) in range(6, 20):
        print(f"{number} лет")
    elif int(number) % 10 == 1 & int(number) != 11:
        print(f"{number} год")
    else:
        print(f"{number} года")


append_word_to_age()
