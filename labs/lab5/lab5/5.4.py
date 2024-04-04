import random
group1 = ["а", "б", "в", "г", "д", "е", "ё", "ж", "з", "Иванов"]
group2 = ["и", "й", "к", "л", "м", "н", "о", "п", "р", "Иванов"]

teamold = (1, 2, 3, 4, 5)
teamlist = list(teamold)
for i in range(5):
    t = random.randint(1,2)
    if t == 1:
        teamlist[i] = random.choice(random.sample(group1,10))
    else:
        teamlist[i] = random.choice(random.sample(group2,10))
team = tuple(teamlist)


print(group1, "\n", group2, "\n", team)
print(len(team))
sorted_team = tuple(sorted(team))
print("Сортированная команда: ", sorted_team)

print("Ивановых в команде ", sorted_team.count("Иванов")) if "Иванов" in sorted_team else print("Иванов не в команде")