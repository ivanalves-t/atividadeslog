sexo = input('Digite "m" para masculino e "f" para feminino ')
altura = float(input('Digite sua altura no formato "x.xx" '))

m = (72.7*altura)-58
f = (92.1*altura)-44.7

if sexo == 'm':
    print(f'O seu peso ideal é {m}Kg')
elif sexo == "f":
    print(f'O seu peso ideal é {f}Kg')
else:
    print('Digite apenas "m" ou "f"')
    