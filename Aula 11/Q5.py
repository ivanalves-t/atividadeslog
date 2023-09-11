'''
Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se feita da
direita para esquerda ou vice-versa. Por exemplo: OSSO e OVO são palíndromos. Em
textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO
ONIBUS é o exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que leia uma seqüência de caracteres, mostre-a e diga se é um
palíndromo ou não.
'''

str1 = input('Digite uma palavra ')
palin = ''
no_space = str1.replace(' ','')

for i in range(len(no_space)):
    palin += no_space[-i-1]

if palin == no_space:
    print(f'"{str1}" é igual escrito de trás pra frente. Logo, é palíndromo')
else:
    print('Não é palíndromo')
