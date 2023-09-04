'''
Escreva um programa que leia um número inteiro e calcule a soma de todos
os divisores desse número, com exceção dele próprio. Ex: a soma dos
divisores do número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78
'''

num = int(input('Type the number'))
resultado = 0

print(f'A soma dos divisores do número {num} é: ',end='')

for i in range(1,num+1):
    if num % i ==0:
        resultado += i
        if i != num:
            print(f'{i} + ', end='')
        if i == num:
            print(f'{i} = ', end='')

print(resultado)
print(f'Mas, como é pra desconsiderar o último, coisa que não faz sentido. Fica: {resultado-num}')
