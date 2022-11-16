numbers = []
count = int(input('Введите количество элементов: '))
for i in range(count):
    i += 1  # чтобы выводил не с 0 запрос на ввод
    numbers.append(input(f'Введите {i} элемент: '))
    i -= 1  # backup чтобы не сломалось
numbers.sort()
print(numbers)
