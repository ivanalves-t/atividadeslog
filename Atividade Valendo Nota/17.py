km = float(input('Digite a distância percorrida '))
l = float(input('Digite o gasto de gasolina consumida nessa distância '))

consumo = km/l

if consumo < 8:
    print('Venda o carro!')
elif consumo >=8 and consumo <= 12:
    print('Econômico')
else:
    print('Super econômico')
