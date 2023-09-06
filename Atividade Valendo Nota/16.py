age = int(input('Digite a idade do trabalhador '))
time_job = int(input('Digite o tempo de serviço '))

if age >= 65 or time_job >= 30:
    print('Pode se aposentar')
elif age >= 60 and time_job >= 25:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
    