import random
import time

def guess_the_number():
    # Випадковим чином обирається число від 1 до 100
    secret_number = random.randint(1, 100)
    previous_difference = None  # Зберігається різниця між попереднім та поточним варіантом
    attempts = 0  # Лічильник спроб
    start_time = time.time()  # Запам'ятовування часу початку гри
    
    print("Вгадайте число від 1 до 100.")

    while True:
        user_input = input("Введіть ваш варіант або 'стоп' для завершення гри: ").lower()

        if user_input == 'стоп':
            print("Грайте ще.")
            break

        try:
            user_number = int(user_input)
        except ValueError:
            print("Некоректне значення! Введіть число в діапазоні від 1 до 100 або 'стоп' для завершення гри.")
            continue

        if not 1 <= user_number <= 100:
            print("Введіть значення в діапазоні від 1 до 100.")
            continue

        difference = abs(secret_number - user_number)
        attempts += 1

        if difference == 0:
            end_time = time.time()
            print(f"ПЕРЕМОГА!!! Ви вгадали число {secret_number} за {attempts} спроб. Гра тривала {int(end_time - start_time)} секунд.")
            break
        elif attempts == 1:
            if difference <= 10:
                print("Дуже тепло!")
            elif 11 <= difference <= 20:
                print("Тепло")
            else:
                print("Холодно")
        else:
            if difference < previous_difference:
                print("Тепліше!")
            else:
                print("Холодніше!")

        previous_difference = difference

# Пуск гри
guess_the_number()
