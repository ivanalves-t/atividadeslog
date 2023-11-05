'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
'''

cobertura_tinta = 3
preco_tinta = 80.00
litros_lata = 18

area_a_pintar = float(input('Digite aqui, a área que você deseja pintar '))

litros_necessarios = area_a_pintar / cobertura_tinta
latas_necessarias = int(litros_necessarios/litros_lata)

if litros_necessarios % litros_lata != 0:
    latas_necessarias += 1

preco = latas_necessarias * preco_tinta

print(f'A quantidade de latas de tinta necessárias são: {latas_necessarias}')
print(f'E o preço total é: R$ {preco}')
