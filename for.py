# list
friends = ['maks', 'kate', 'ivan', 'dima', 'lev']

for friend in friends:
    print(friend)

# str
fried_str = 'maksim olegov'
for letter in fried_str:
    print(letter)

# dict
friend = {
    'name': 'Max',
    'age': 20,
    'has_car': True
}

# без ключей
for key in friend:
    print(key)
    print(friend[key])
# только значение
for v in friend.values():
    print(v)

# по парам ключ значение
for item in friend.items():
    print(item)

for key, val in friend.items():
    print(key)
    print(val)

name, age, has_car = {'ivan', 40, True}
print(name, age, has_car)


friends = ['maks', 'kate', 'ivan', 'dima', 'lev']
for friend in friends[:3]:
    print(friend)