'''
Uma empresa concederá um aumento de salário aos seus funcionários,
variável de acordo com o cargo, conforme a tabela abaixo. Faça um
programa que leia o salário e o código do cargo de um funcionário e calcule
o seu novo salário. Se o cargo do funcionário não estiver na tabela, ele
deverá, então, receber 15% de aumento. Mostre o salário antigo, o novo
salário e a diferença entre ambos.
'''

salario = float(input('Digite seu salário:'))
codigo = float(input('Agora digite seu código'))

if codigo == 310:
    reajuste = 105/100
elif codigo == 456:
    reajuste = 107.5/100
elif codigo == 885:
    reajuste = 110/100
else:
    reajuste = 115/100

print(f'O salário do código {codigo} foi reajustado em {reajuste}%, sendo agora: R${salario*reajuste:.2f}')
