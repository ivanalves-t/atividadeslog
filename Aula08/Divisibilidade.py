'''
Solicite um número ao usuário. Se for divisível por 3, informe “é divisível por 3”. Se
for divisível por 4, informe “é divisível por 4”. Se for divisível por 3 e 4, informe “É
divisível tanto por 3 quanto por 4”.
'''
num = int(input('Digite o número'))

if num %3 == 0 and num %4 == 0:
    print('O número é divisível por 3 e por 4')
elif num %3 == 0:
    print('O número é divisivel apenas por 3')
elif num %4 == 0:
    print('O número é divisivel apenas por 4')
else:
    print('O número não é divisivel por 3 nem por 4')
