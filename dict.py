# словари
name = 'max'
age = 20
has_car = True

# friend = (name, age, has_car)
# friend_inverse = (age, name, has_car)

# Объявление
friend = {
    'name': 'Max',
    'age': 20,
    'has_car': True
}

print(type(friend))

# индексы нот тудей, юзаем ключи

print(friend)
print(friend['name'])
print(friend['has_car'])

# функции
print(len(friend))

# оператор вхождения. Проверяет по ключам
print('name' in friend)

# методы добавить измен удалить

print(friend)
friend['has_wife'] = False
print(friend)
friend['has_wife'] = True
print(friend)

# удалить
del friend['has_wife']
print(friend)

# ключи
print(friend.keys())
print(friend.values())
print(friend.items())

print(20 in friend.values())
# методы
