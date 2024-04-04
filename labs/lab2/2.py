place = int(input())
if place % 2 == 0:
    high = "верхнее"
else:
    high = "нижнее"
if 52 >= place >= 37:
    pos = "боковое место"
else:
    pos = "место в купе"
print(place, " - ", high, pos)