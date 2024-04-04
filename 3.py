word = ''
while word != 'stop':
    word = input('Введите слово и я проверю его на редкость! ')
    if 'ф' in word:
        print('Ого! Это редкое слово!')
    else:
        print("Эх, это не очень редкое слово...")
        