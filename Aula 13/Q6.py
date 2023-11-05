'''
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um
crime. As perguntas são:
 "Telefonou para a vítima?"
 "Esteve no local do crime?"
 "Mora perto da vítima?"
 "Devia para a vítima?"
 "Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da pessoa no
crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como
"Suspeita"

, entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será

classificado como "Inocente".
'''
culpometroN = 0

questions = {
0 : 'Telefonou para a vítima?',
1 : 'Esteve no local do crime?',
2 : 'Mora perto da vítima?',
3 : 'Devia para a vítima?',
4 : 'Já trabalhou para a vítima?'
}

for i in range(5):
    culpometroStr = ''
    culpometroStr = input(f'{questions[i]}').lower()
    if culpometroStr == 's':
        culpometroN += 1
print()

if culpometroN == 5:
    print('Assasino')
elif culpometroN == 3 or culpometroN == 4:
    print('Cúmplice')
elif culpometroN <=2 and culpometroN != 0:
    print('Suspeito')
else:
    print('Inocente')