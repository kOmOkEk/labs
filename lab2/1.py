a = input()
b = input()
if len(a) >= 8:
    if a == b:
        print("Пароль принят")
    else:
        print("Пароль не принят")
else:
    print("Пароль слишком короткий")

