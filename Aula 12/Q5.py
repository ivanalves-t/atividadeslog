'''
Modifique o programa da questão 3 para que o programa funcione para qualquer
quantidade de alunos. Assim, durante a leitura das idades e alturas o usuário poderá inserir
um valor negativo para indicar que deseja interromper a leitura dos dados.
'''
list_students_height = []
list_students_age = []
midgets = 0
count = 0

while True:
    age = int(input('Digite a idade: '))
    height = float(input('Digite a altura: '))
    if age and height >=0:
        count += 1
        list_students_age.append(age)
        list_students_height.append(height)
    elif age or height <0:
        break

mid_height = sum(list_students_height)/count

for j, k in zip(list_students_age,list_students_height):
    if j > 13 and k < mid_height:
        midgets += 1

if midgets == 0:
    print('Nenhum aluno maior de 13 anos possui altura menor que a média')
elif midgets > 0:
    print('A quantidade de alunos maiores de 13 anos com altura inferior à média é {} alunos'.format(midgets))
