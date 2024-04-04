def mixed(color1, color2):
    if color1 == "красный" and color2 == "синий" or color2 == "красный" and color1 == "синий":
        return "фиолетовый"
    if color1 == "красный" and color2 == "желтый" or color2 == "красный" and color1 == "желтый":
        return "оранжевый"
    if color1 == "синий" and color2 == "желтый" or color2 == "синий" and color1 == "желтый":
        return "зеленый"

ls = list("красный", "синий", "желтый")
color1 = str(input("Введите цвет(красный, синий или желтый)"))
color2 = str(input("Введите цвет(красный, синий или желтый)"))
if color1 == any(ls):
    print(mixed(color1, color2))
else:
    print("неправильный цвет")
