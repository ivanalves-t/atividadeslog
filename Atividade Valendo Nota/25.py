soma_par = 0
produto_impar = 1

num1 = int(input('Digite um número '))
num2 = int(input('Digite outro número '))

if num1 > num2:
    num1, num2 = num2, num1

for num1 in range(num1,num2+1):
    if num1 %2 == 0:
        soma_par += 1
    else:
        produto_impar *= num1       

print(f'A soma dos números pares do intervalo é {soma_par}')
print(f'A multiplicação dos ímpares do intervalo é {produto_impar}')
