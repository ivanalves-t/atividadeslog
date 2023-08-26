'''
Crie um programa em Python que que solicite ao usuário e receba o valor do raio
para calcular a área, perímetro e diâmetro de um círculo;
. Declare π como constante.
'''

PI = 3.14
raio = float(input('Digite o valor do raio'))
perimetro = 2*PI*raio
diametro = 2*raio
area = PI*(raio**2)

print(f'A área é {area}. O perimetro é {perimetro}. A área do círculo é {area}')
