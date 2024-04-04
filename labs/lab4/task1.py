def division_by_three(i):
    if i % 3 == 0:
        return "The number is divisible by 3"
    else:
        return "The number isn't divisible by 3"

print(division_by_three(int(input("Введите число для проверки  "))))

