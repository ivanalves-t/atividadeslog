'''
Registro de alunos: Crie um programa que registre os dados dos alunos de
uma turma, incluindo nome, idade e notas. Utilize uma lista de tuplas para
armazenar os registros dos alunos e permita a busca de um aluno pelo nome.
'''
alunos = {}

while True:
    nomes = input('Nome: ')
    idades = input('Idade: ')
    notas = input('Notas: ')
    alunos[nomes] = (f'Nome: {nomes}, Idade: {idades}, Notas: {notas}')
    print()
    cont = input("Deseja continuar? 'S' ou 'N'? ").upper()
    print()
    if cont == 'N': break

busca = input('Digite o Nome do aluno para Busca: ')
print()

if busca in alunos:
    print(alunos[busca])
else:
    print(f'O aluno "{busca}" não foi registrado.')