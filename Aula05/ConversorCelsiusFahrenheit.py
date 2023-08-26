'''
5. Faça um Programa que dada a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
'''

temp_fahrenheit = float(input('Digite a temperatura em F'))
temp_celsius = (temp_fahrenheit-32)*5/9

print(f'A temperatura {temp_fahrenheit} F, convertida em celsius é de: {temp_celsius:.1f}')
