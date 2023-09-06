i = 0
print('Responda honestamente: "s" para sim ou "n" para não ')

call_victm = input('Telefonou para a vítima? ')
if call_victm == 's':
    i += 1
stay = input('Esteve no local do crime? ')
if stay == 's':
    i += 1
live = input('Mora perto da vítima? ')
if live == 's':
    i += 1
dues = input('Devia para a vítima? ')
if dues == 's':
    i += 1
job = input('Já trabalhou com a vítima? ')
if job == 's':
    i += 1

if i >= 2:
    if i ==2:
        print('Suspeito')
    if i >= 3 and i <= 4:
        print('Cúmplice')
    if i == 5:
        print('Assasino')
else:
    print('Inocente')
