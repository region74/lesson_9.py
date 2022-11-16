# как было
new_numbers = input('Введите элементы списка через запятую: ')

new_list = new_numbers.replace(',', ' ').replace(';', ' ').replace('/', ' ').split()

new_set = set(new_list)
sort_list = list(new_set)
sort_list.sort()
print(sort_list)

# разбор как должно быть
example_list = []
for number in new_list:
    if new_list.count(number) == 1:
        example_list.append(number)

print(example_list)
