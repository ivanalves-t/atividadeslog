#NÃO USE MAIS TANTOS ELIFS

'''
Faça um programa que leia uma data de nascimento no formato
dd/mm/aaaa e imprima a data com o mês escrito por extenso. Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995
'''

birth_date = input('Digite a data do seu nascimento no formato dd/mm/aaaa ')
extenso = ''
#NÃO USE MAIS TANTOS ELIFS
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

if birth_date[3:5] in meses_ano:
    extenso = meses_ano[birth_date[3:5]]


print(f'Você nasceu em {birth_date[0:2]} de {extenso} de {birth_date[6:]}')

"""
date_birth = input('Digite a data do seu nascimento no formato dd/mm/aaaa ')
extenso = ''


if date_birth[3:5] == '01':
    extenso += "Janeiro"
elif date_birth[3:5] == '02':
    extenso += 'Fevereiro'
elif date_birth[3:5] == '03':
    extenso += 'Março'
elif date_birth[3:5] == '04':
    extenso += 'Abril'
elif date_birth[3:5] == '05':
    extenso += 'Maio'
elif date_birth[3:5] == '06':
    extenso += 'Junho'
elif date_birth[3:5] == '07':
    extenso += 'Julho'
elif date_birth[3:5] == '08':
    extenso += 'Agosto'
elif date_birth[3:5] == '09':
    extenso += 'Setembro'
elif date_birth[3:5] == '10':
    extenso += 'Outubro'
elif date_birth[3:5] == '11':
    extenso += 'Novembro'
elif date_birth[3:5] == '12':
    extenso += 'Dezembro'

print(f'Você nasceu em {date_birth[0:2]} de {extenso} de {date_birth[6:]}')
"""
