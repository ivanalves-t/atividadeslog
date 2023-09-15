'''
Número por extenso. Escreva um programa que solicite ao usuário a
digitação de um número até 99 e imprima-o na tela por extenso.
'''
str1 = input('Digite um número de 0 a 99 ')
str2 = ''
number_str = {
'0' : 'zero',
'1' : 'um',
'2' : 'dois',
'3' : 'três',
'4' : 'quatro',
'5' : 'cinco',
'6' : 'seis',
'7' : 'sete',
'8' : 'oito',
'9' : 'nove',
'10': 'dez',
'11': 'onze',
'12': 'doze',
'13': 'treze',
'14': 'catorze',
'15': 'quinze',
'16': 'dezesseis',
'17': 'dezessete',
'18': 'dezoito',
'19': 'dezenove',
'20': 'vinte',
'30': 'trinta',
'40': 'quarenta',
'50': 'cinquenta',
'60': 'sessenta',
'70': 'setenta',
'80': 'oitenta',
'90': 'noventa'
}

if len(str1) == 2 and str1[-1] != '0' and str1[0] != '1':
    str2 = str1[:-1] + '0'
    print(f'{number_str[str2]} e {number_str[str1[1]]}')

else:
    print(number_str[str1])
