nota1 = int(input('Digite uma nota '))
nota2 = int(input('Digite a segunda nota '))

if nota1 <0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('DIGITE DUAS NOTAS VÁLIDAS')
else:
    print(f'A média é {(nota1+nota2)/2}')
    