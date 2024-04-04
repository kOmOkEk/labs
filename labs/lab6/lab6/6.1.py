capitals = {"Россия" : "Москва", "Нидерланды" : "Амстердам", "Анкара" : "Турция", "Сербия" : "Белград", "Франция" : "Париж"}
print(capitals)
guess = input("Введите страну: ")
if guess in capitals:
    print(capitals[guess])
else:
    print("Такой страны нет в списке")
sortedCapitals = sorted(capitals.items(), key=lambda item: item[0])
print(sortedCapitals)