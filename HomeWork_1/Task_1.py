def even_numbers_sum(number):
    even_sum = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even_sum += int(digit)
    return even_sum


def odd_numbers_sum(number):
    odd_sum = 0
    for digit in number:
        if int(digit) % 2 != 0:
            odd_sum += int(digit)
    return odd_sum


def numbers_sum():
    number = int(input("Введите целое число в диапазоне от 0 до 10 в 20 степени: "))
    if number >= 0 & number <= 10 ** 20:
        print(f"Результат - {odd_numbers_sum(str(number))} {even_numbers_sum(str(number))}")


numbers_sum()
