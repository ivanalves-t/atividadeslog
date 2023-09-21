'''Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 - Janeiro, 2 - Fevereiro, . . . ).
'''
temp_list = []
above_temp_list = []
meses_ano = {
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
for i in range(1,13):
    month = input(f'Digite a temperatura do mês de {meses_ano[str(i)]}: ')
    temp_list.append(month)

mid_temp = sum(temp_list)/12
for i in temp_list:
    if i > mid_temp:
        above_temp_list.append(meses_ano[str(i)])
        above_temp_list.append(i)

if above_temp_list == 0:
    print('Não houve meses com temperatura acima da média')
else:
    print(f'Lista dos meses com temperatura acima da média: {above_temp_list}')
