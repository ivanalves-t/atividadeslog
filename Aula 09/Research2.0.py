'''
A prefeitura de uma cidade deseja fazer uma pesquisa entre seus habitantes.
Faça um algoritmo para coletar e armazenar dados sobre o salário e número
de filhos de cada habitante e após as leituras, escrever:
a) Média de salário da população
b) Média do número de filhos
c) Maior salário dos habitantes
d) Percentual de pessoas com salário menor que R$ 150,00

Obs.: O final da leituras dos dados se dará com a entrada de um “salário negativo”.
'''

salario_populacao = []
num_filhos = []
less150 = 0

while(True):
    sal = float(input('Digite o salário do entrevistado '))
    if sal < 0:
        break
    filhos = float(input('Digite a quantidade de filhos '))
    num_filhos.append(filhos)
    salario_populacao.append(sal)
    if sal < 150:
        less150 +=1
    
media_filhos = sum(num_filhos)/len(num_filhos)
media_salario = sum(salario_populacao)/len(salario_populacao)
bigger_payment = max(salario_populacao)
people_less150 = less150 * 100 / len(salario_populacao)

print(f'A média de salário da população é: R${media_salario}')
print(f'A média do número de filhos foi: {media_filhos}')
print(f'O maior salário foi: R${bigger_payment}')
print(f'A porcentagem de pessoas com salario abaixo de R$150,00 foi: {people_less150}%')
