'''
Crie um programa em Python que solicite ao usuário e receba os valores da base
e altura para calcular a área de um triangulo;
'''
valor_base = float(input('Digite o valor da base'))
valor_altura = float(input('Digite o valor da altura'))

area_triangulo = (valor_base*valor_altura)/2

print(f'O valor da area do triangulo é {area_triangulo:.1f} cm2')
