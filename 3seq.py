import copy

# как было
new_numbers = input('Введите элементы первого списка через запятую: ')
first_list = set(new_numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split())

new_numbers = input('Введите элементы второго списка через запятую: ')
second_list = set(new_numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split())

print(first_list - second_list)

# ч должно быть

# это наверх чтобы данные не затерлись
first_tmp = new_numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()
second_tmp = new_numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()

# копия списка
# first_tmp[:]
# first_tmp.copy()
# copy.deepcopy(first_tmp)


for tmp in first_tmp[:]:
    if tmp in second_tmp:
        first_tmp.remove(tmp)

print(first_tmp)
