'''
A série de Fibonacci é formada pela seqüência 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ... Faça um programa capaz de gerar a série até o n-ésimo termo. 10. A série de Fibonacci é formada pela seqüência 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,
55,... Faça um programa que gere a série até que o valor seja maior que 500. 11.
'''

num = int(input("Digite o número de termos da sequência de Fibonacci: "))

previous = 0
current = 1
print(f'{previous} ')


for i in range(num):
    print(current)
    previous, current = current, previous + current
