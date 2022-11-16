result = range(1, 10)
print(result)

result = range(4, 30, 2)
result = range(60, 2, -4)
print(list(result))

for i in range(10):
    print(i)

# индексация списка

questions = ['a', 'b', 'c']
answers = [1, 3, 4]

for i in range(len(questions)):
    print(i)
    print(questions[i])
    print(answers[i])

# enumerate
for i, q in enumerate(questions):
    print(i)
    print(q)
