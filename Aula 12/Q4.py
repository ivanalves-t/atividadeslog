'''
Modifique o programa da questão 3 para que o usuário indique a quantidade de alunos que
será utilizada no programa. Assim antes de começar a leitura de idades e alturas, o programa
deve solicitar ao usuário o quantitativo de alunos.
'''
q_alunos = int(input('Digite a quantidade de alunos da pesquisa: '))
list_students_height = []
list_students_age = []
midgets = 0

for i in range(q_alunos):
    age = int(input('Digite a idade: '))
    list_students_age.append(age)
    height = float(input('Digite a altura: '))
    list_students_height.append(height)

mid_height = sum(list_students_height)/q_alunos

for j in range(q_alunos):
    if list_students_age[j] > 13 and list_students_height[j] < mid_height:
        midgets += 1

if midgets == 0:
    print('Nenhum aluno maior de 13 anos possui altura menor que a média')
elif midgets > 0:
    print('A quantidade de alunos maiores de 13 anos com altura inferior à média é {} alunos'.format(midgets))
