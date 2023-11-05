'''Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).
'''
temp_above = []
i = 1
mid_month = 0
temp_list = []
month_attrib = {
'1' : 'Janeiro',
'2' : 'Fevereiro',
'3' : 'Março',
'4' : 'Abril',
'5' : 'Maio',
'6' : 'Junho',
'7' : 'Julho', 
'8' : 'Agosto',
'9' : 'Setembro',
'10' : 'Outubro',
'11' : 'Novembro',
'12' : 'Dezembro',
}

while i < 13:
    month = int(input(f'Digite a temperatura do mês de {month_attrib[str(i)]}: '))
    mid_month += month
    i += 1
    temp_list.append(month)

mid_month /= 12

for i,j in zip(temp_list,range(1,12)):
    if i > mid_month:
        print(f'{month_attrib[str(j)]}: {i} graus')
        