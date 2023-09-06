real = float(input('Digite o valor em Real Brasileiro '))
dolar = float(input('Digite a cotação atual do dólar '))

cambio = real/dolar
#Formatei em 2 casas decimais para representar os centavos
print(f'R${real} equivale a ${cambio:.2f}')
