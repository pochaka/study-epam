from random import randint

number = randint(1, 101)
guessed_number = None

print("Угадай число между 1 и 100")

while number != guessed_number:
    try:
        guessed_number = int(input("Ваше число: "))
    except ValueError:
        print("Вы ввели не число.")
    if number == guessed_number:
        print("Победа!")
        