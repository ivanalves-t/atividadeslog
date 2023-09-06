resultado = 0
positive = 0

for i in range (1,11):
    num = int(input('Digite um valor '))
    if num > 0:
        resultado += num
        positive += 1 

print(f'A média dos números positivos digitados é {resultado/positive}')
