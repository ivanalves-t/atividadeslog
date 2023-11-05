num = input('Digite um número de 4 algarismos: ')
soma = 0

if len(num) != 4:
    print('Erro! Digite um número de 4 algarismos! ')

else:
    soma = float(num[0:2])+float(num[2:])

    if soma == int(num) ** 0.5:
        print(f'n = {num}, dezenas de n = {num[0:2]} + {num[2:]}, soma das dezenas = {soma}, raiz quadrada de n = {soma}')
        print(f'Portanto, a raiz quadrada de {num} é igual a soma de suas dezenas. ')

    else:
        print('O número tem raiz diferente da soma de suas dezenas ')