"""
O IMC (índice de massa corpórea) indica o grau de obesidade de uma pessoa. Este
índice é obtido pelo peso (em kg) dividido pelo quadrado da altura (em metros). A
tabela a seguir apresenta as faixas deste índice:
"""

peso_valor = float(input('Digite seu peso'))
altura_valor = float(input('Digite sua altura'))
imc = peso_valor / altura_valor**2

if imc < 20:
    print(f'{imc} equivale a peso Abaixo do normal')
elif imc >= 20 and imc < 25:
    print(f'{imc} equivale a Peso normal')
elif imc >= 25 and imc < 30:
    print(f'{imc} equivale a Sobrepeso')
elif imc >= 30 and imc < 35:
    print(f'{imc} equivale a Obesidade leve')
elif imc >= 35 and imc < 40:
    print(f'{imc} equivale a Obesidade moderada')
else:
    print(f'{imc} equivale a Obesidade mórbida')
