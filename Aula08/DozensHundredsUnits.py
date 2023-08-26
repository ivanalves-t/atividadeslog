'''
Faça um Programa que leia um número inteiro menor que 1000 e imprima a
quantidade de centenas, dezenas e unidades do mesmo. Observe os termos no plural, a colocação do "e"
, da vírgula,etc.  Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades
Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21,
11, 1, 7 e 16
'''
num = int(input('Digite um número menor que 1000 '))

unidade = num % 10
dezena = (num%100)//10
centena = num //100
plural = 's'

if centena > 1:
    print(centena,'centena'+plural)
elif centena == 1:
    print(centena,'centena')
else:
    print(end='')
    
if dezena > 1:
    print(dezena,'dezena'+plural)
elif dezena == 1:
    print(dezena,'dezena')
else:
    print(end='')

if unidade > 1:
    print(unidade,'unidade'+plural)
elif unidade == 1:
    print(unidade,'unidade')
else:
    print(end='')
