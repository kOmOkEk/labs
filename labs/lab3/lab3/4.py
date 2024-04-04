import random

a = 0
b = 0
answer = ''
score = 0
life = 3
while life != 0:
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    answer = input(f"{a} + {b} = ")
    if int(answer) == a + b:
        print("Правильно!")
        score += 1
    else:
        print("Неправильно(((")
        life -= 1
    if life == 0:
        print("Конец игры")
        print(f"Ваш счёт: {score}")
