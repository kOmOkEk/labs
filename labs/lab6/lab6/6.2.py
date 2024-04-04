mydict = {"а": " ", "б": " ", "в": " ", "г": " ", "д": " ", "е": " ", "ё": " ", "ж": " ", "з": " ", "и": " ", "й": " ",
          "к": " ", "л": " ", "м": " ", "н": " ", "о": " ", "п": " ", "р": " ", "с": " ", "т": " ", "у": " ", "ф": " ",
          "х": " ", "ц": " ", "ч": " ", "ш": " ", "щ": " ", "ъ": " ", "ы": " ", "ь": " ", "э": " ", "ю": " ", "я": " "}

score1 = ("а", "в", "е", "и", "н", "о", "р", "с", "т")
score2 = ("д", "к", "л", "м", "п", "у")
score3 = ("б", "г", "ё", "ь", "я")
score4 = ("й", "ы")
score5 = ("ж", "з", "х", "ц", "ч")
score8 = ("ш", "э", "ю")
score10 = ("ф", "щ", "ъ")

for i in mydict:
    if any(i == a for a in score1) == True:
        mydict[i] = 1
    if any(i == b for b in score2) == True:
        mydict[i] = 2
    if any(i == c for c in score3) == True:
        mydict[i] = 3
    if any(i == d for d in score4) == True:
        mydict[i] = 4
    if any(i == j for j in score5) == True:
        mydict[i] = 5
    if any(i == e for e in score8) == True:
        mydict[i] = 8
    if any(i == f for f in score10) == True:
        mydict[i] = 10


example = str(input("Введите слово: "))
price = 0
for i in example:
    price = price + mydict[i]

print(price)
