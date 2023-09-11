'''
Faça um programa que leia uma data de nascimento no formato
dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995
'''
"""
date_birth = input('Digite a data do seu nascimento no formato dd/mm/aaaa ')
extenso = ''

meses_ano = {
'01' : 'Janeiro',
'02' : 'Fevereiro',
'03' : 'Março',
'04' : 'Abril',
'05' : 'Maio',
'06' : 'Junho',
'07' : 'Julho', 
'08' : 'Agosto',
'09' : 'Setembro',
'10' : 'Outubro',
'11' : 'Novembro',
'12' : 'Dezembro',
}

if date_birth[3:5] in meses_ano:
    extenso = meses_ano[date_birth[3:5]]


print(f'Você nasceu em {date_birth[0:2]} de {extenso} de {date_birth[6:]}')
"""

str1 = input('Digite aqui a string ')

print('Na string existem ',str1.count('a'),'vogais')