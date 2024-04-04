week = 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'

ask = int(input('Сколько выходных на неделе Вы хотите?'))

print("Ваши выходные дни: ", week[-ask:])
print("Ваши рабочие дни: ", week[:-ask])