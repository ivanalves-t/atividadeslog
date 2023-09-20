'''
Faça um programa que leia 10 números inteiros. Cada numero par deve ser armazenado em
uma lista de pares e cada impar tem que ser armazenado em uma lista de impares. Ao
término do programa imprima as duas listas.
'''
i = 0
int_even_list = []
int_odd_list = []

while i < 10:
    i +=1
    num = int(input('Digite um número: '))
    if num %2 == 0:
        int_even_list.append(num)
    else:
        int_odd_list.append(num)

print(f'A lista de números pares é {int_even_list}. A lista de números ímpares é {int_odd_list}')
