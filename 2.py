result = ''
p = ''
while p != 'stop':
    p = input("Введите слово: ")
    if p != 'stop':
        result += ' ' + p
print(result)