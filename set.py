# set

office = {'roma', 'slava', 'slava', 'ivan'}
print(office)

# уникальность
print(set(office))

# операции с множествами

office = {'roma', 'slava', 'slava', 'ivan'}
freelance = {'kate', 'oleg', 'pavel', 'ivan'}
# только офис
print(office - freelance)
# только фриланс
print(freelance - office)
# везде
print(freelance & office)
