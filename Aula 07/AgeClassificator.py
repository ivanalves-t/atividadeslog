'''
Elaborar um algoritmo que, dada a idade de um nadador, classificá-lo nas
categorias: infantil A (5 - 7 anos), infantil B (8 -10 anos), juvenil A (11 - 13
anos), juvenil B (14 -17 anos) e adulto (maiores que 18 anos).

'''

age = int(input('Digite a idade'))

if age >= 5 and age <= 7:
     print('Infantil A')
elif age >= 8 and age <= 10:
     print('Infantil B')
elif age >= 11 and age <=13:
     print('Juvenil A')
elif age >= 14 and age <=17:
     print('Juvenil B')
else:
     print('Adulto')
