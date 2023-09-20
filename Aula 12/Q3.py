'''
Faça um programa que armazene as idades e as alturas de 4 alunos. Seu programa deve
exibir quantos alunos com mais de 13 anos possuem uma altura inferior à altura média
dentre todos os alunos.
'''
list_students_height = []
list_students_age = []
midgets = 0

for i in range(4):
    age = int(input('Digite a idade: '))
    list_students_age.append(age)
    height = float(input('Digite a altura: '))
    list_students_height.append(height)

mid_height = sum(list_students_height)/4

for j, k in zip(list_students_age,list_students_height):
    if j > 13 and k < mid_height:
        midgets += 1

if midgets == 0:
    print('Nenhum aluno maior de 13 anos possui altura menor que a média')
elif midgets > 0:
    print('A quantidade de alunos maiores de 13 anos com altura inferior à média é {} alunos'.format(midgets))
