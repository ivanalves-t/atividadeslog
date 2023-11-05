'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer
número inteiro entre 1 a 10. O usuário deve informar de qual numero ele
deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
'''

numero = int(input('Digite o número '))

i = 1

while i <= 10:
    resultado = numero * i
    print(f'{numero} X {i} = {resultado}')
    i += 1
