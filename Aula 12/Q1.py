'''
Faça um Programa que leia 5 números inteiros, armazene-os em uma lista e imprima essa
lista na tela.
'''
int_list = []
i = 0

while i < 5:
    i += 1
    int_list.append(input('Type a number: '))

print(int_list)
