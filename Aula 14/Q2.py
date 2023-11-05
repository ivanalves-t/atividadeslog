lista = list(map(int, input('ENTRADA: ').split(',')))
resultado = [(val, pow(val, 3)) for val in lista] 
print(f'RESULTADO: {resultado}') 