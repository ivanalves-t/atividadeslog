'''
Escreva um algoritmo para ler as dimensões de uma cozinha retangular
(comprimento, largura e altura) e em seguida, calcular e escrever a quantidade de
caixas de azulejos para se colocar em todas as suas paredes (considere que não será
descontada a área ocupada por portas e janelas). Cada caixa de azulejos possui 1,5
m2.
'''

a = float(input('Digite o comprimento '))
b = float(input('Agora digite a largura '))
c = float(input('Digite a altura '))

resultado = ((2*(a*b)+(a*c)+(b*c))-(a*b))//1.5

print(f'A quantidade de caixas de azulejos foi: {resultado:.0f}')
