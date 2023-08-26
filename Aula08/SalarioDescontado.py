'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os
descontos são do Imposto de Renda, que depende do salário bruto (conforme
alíquotas abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do
Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido
corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao
usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
'''

payment = float(input('Digite o valor da hora trabalhada'))
hour_worked = float(input('Digite a quantidade de horas trabalhadas por mês'))
payment_brute = payment * hour_worked*18.19


sindicato = 3/100
fgts = 11/100
inss = 10/100

if payment_brute <= 900:
    desconto_ir = 0
elif payment_brute > 900 and payment_brute <= 1500:
    desconto_ir = 5/100
elif payment_brute > 1500 and payment_brute <= 2500:
    desconto_ir = 10/100
else:
    desconto_ir = 20/100

total_descontos = (payment_brute*sindicato)+(payment_brute*inss)+(payment_brute*desconto_ir)

print(f'Salário bruto: R${payment_brute}')
print(f'(-) IR  : R${payment_brute*desconto_ir}')
print(f'(-) INS{inss*100}   : R${payment_brute*inss}')
print(f'(-) Sindicato{sindicato*100}%)  : R${payment_brute*sindicato}')
print(f'FGTS{fgts*100}% : R${payment_brute*fgts}')
print(f'Total de descontos: R${total_descontos}')
print(f'Salário Líquido : R${payment_brute-total_descontos}')
