friends = ['maks', 'kate', 'ivan', 'dima', 'lev']

print(friends[1])
print(friends[1:])

# функции
print(len(friends))

# оператор вхождения
print('lev' in friends)

# методы основные

# добавление
friends.append('kamil')
print(friends)

friends.insert(2, 'kris')
print(friends)

# удаление
friends.remove('dima')
print(friends)

# изменение

friends[3] = 'leonid'
print(friends)

# удаление по индексу
del friends[2]
print(friends)
friends.sort()

print(friends)
friends.reverse()
print(friends)

