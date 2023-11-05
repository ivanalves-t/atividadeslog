'''Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e
armazene os resultados em uma lista. Utilize uma lista de contadores (1-6) e depois
da execução dos sorteios, mostre quantas vezes cada valor foi conseguido.  Dica: sorteios em python podem ser realizados através da biblioteca random,
pelas funções randint() e randrange().  Documentação: https://docs.python.org/pt-br/3.8/library/random.html'''

dados = []
import random

for i in range(100):
    dados.append(random.randint(1,6))

print(f'Lado 1: {dados.count(1)} vezes')
print(f'Lado 2: {dados.count(2)} vezes')
print(f'Lado 3: {dados.count(3)} vezes')
print(f'Lado 4: {dados.count(4)} vezes')
print(f'Lado 5: {dados.count(5)} vezes')
print(f'Lado 6: {dados.count(6)} vezes')
