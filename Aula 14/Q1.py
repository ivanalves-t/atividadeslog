tupla = (1, 3, 5, 2, 3, 5, 1, 1, 3)

print(f'A tupla original é: {tupla}')
print()
print(f'A tupla após a remoção de duplicatas: {tuple(set(tupla))}')
