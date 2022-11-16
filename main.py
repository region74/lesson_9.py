# Строки

friend = 'maskim aleksandrovich popov'

# кавычкив кавычках
# friend = 'maskim "aleksandrovich" popov'
# friend = 'maskim \'aleksandrovich\' popov'

# print(friend)

# индексы
print(friend[1])
print(friend[3:])
print(friend[3:11])

# отрицательные индексы
print(friend[:-2])
print(friend[1:-1])

# функции и методы строки
# функции
friend = 'maskim aleksandrovich popov'
print(len(friend))

# метод
friend_upper = friend.upper()
print(friend_upper)

# на вхождение подстроки в строку (оператор)
friend = 'maskim aleksandrovich popov'
leters = 'skim'
print(leters in friend)

# методы строк
friend = 'maskim aleksandrovich popov'
# заменим фамилию
# замена подстроки строкой
friend2 = friend.replace('popov', 'ivanov')
print(friend2)
print(friend.replace('popov', 'ivanov'))

# help(str) - расскажет че как
# print(dir(str)) - вывод всех методов
# частые методы
print(friend.upper())
print(friend.lower())
print('title', friend.title())
print(friend.isdigit())
print(friend.split(' '))

goods = 'sasa;;;dsdsdsd;;;dsdsds'
print(goods.split(';;;'))
bad_data = 'stul:divan,auto okno'
print(bad_data.replace(':', ' ').replace(',', ' ').split())

# форматирование строк
# варик 1 (govno)
age = 20
name = 'dima'
info = 'Имя ' + name + 'возраст ' + str(age)
print(info)
# варик 2 +-
info = 'Имя: {} age: {}'.format(name, age)
print(info)

# f строки для трушных пацанов
info = f'Имя {name}, age {age}'
print(info)

# Неизменяемсоть строк. изменяемые и неизмен типы
friend = 'maskim aleksandrovich popov'
friend.upper()
print(friend)
friend=friend.upper() #понял да суть суеты
print(friend)
# friend[0]='G'

l=[]
l.append(1)
print(l)
