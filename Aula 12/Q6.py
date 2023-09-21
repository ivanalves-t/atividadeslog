'''
Faça um programa que leia uma data de nascimento no formato dd/mm/aaaa e
imprima a data com o mês escrito por extenso. Exemplo:
Data = 20/02/1995
Resultado gerado pelo programa:
Você nasceu em 20 de fevereiro de 1995
'''

birth_date = input('Digite a data do seu nascimento no formato dd/mm/aaaa ')
month_int = ''
extence = birth_date.split('/')

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

if month_int [1] in meses_ano:
    extense = meses_ano[month_int[1]]


print(f'Você nasceu em {birth_date[0:2]} de {extense} de {birth_date[6:]}')
