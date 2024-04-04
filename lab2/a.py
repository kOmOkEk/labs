import random

a = 'a', 'b', 'c', 'd'
b = 'e', 'f', 'g', 'i'
request = input("Введите фамилию")
ls = list()

for i in range(5):
    t = random.randint(1,2)
    if t == 1:
        ls.append(random.choice(random.sample(a,4)))
    else:
        ls.append(random.choice(random.sample(b,4)))
if request in ls:
    print("Фамилия в списке!")
else:
    print("Фамилия не в списке((")

print(ls)
'''print(random.sample(a,4))'''