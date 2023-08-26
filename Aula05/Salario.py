'''
Faça um Programa que dado o número de horas trabalhadas e o valor
da hora, calcule e mostre o total do salário no referido mês.
'''

worked_hours = float(input('Digite quantas horas você trabalha por dia'))
price_hours = float(input('Digite o valor da hora trabalhada'))

salario = worked_hours * price_hours * 22

print(f'O salario total é {salario:.2f} reais ao mês')
