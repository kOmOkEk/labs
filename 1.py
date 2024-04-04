N = int(input("Введите количество слов: "))
result = ''
for i in range(N):
    result += ' ' + input("Введите слово: ")
print(result)