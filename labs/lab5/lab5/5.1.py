import random
ls = list()
for i in range(4):
    ls.append(random.randint(1,10))
guess = int(input("Угадайте число: "))
if guess in ls:
    result = "Поздравляю, Вы угадали число!"
else:
    result = "Нет такого числа!"
print(ls)
print(guess)
print(result)