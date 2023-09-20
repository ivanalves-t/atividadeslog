'''
Faça um programa que leia uma palavra e some 1 no valor ASCII de cada
caractere da palavra. Imprima a string resultante.  Dica: O Python disponibiliza 2 funções que são bastante uteis quando estamos
trabalhando com o sistema ASCII. A primeira é a função ord() , que recebe uma
letra como parâmetro e retorna o código ASCII da mesma. A segunda função, é a
chr() , onde passamos o código ASCII e nos é retornado a respectiva letra.  Tabela ASCII: https://www.ime.usp.br/~pf/algoritmos/apend/ascii.html
'''

str1 = input('Digite uma palavra: ')
str2 = ''

for i in str1:
    if i not in str2:
        str2 += i
        print(f'O ASCII de {i} é: {ord(i)+1}')
