#Aluno : Ivanilson Alves Timóteo

#Questão 1
'''
num = int(input('Digite um número inteiro '))

print(num)
'''

#Questão 2
'''
num1 = int(input('Digite um número inteiro '))
num2 = int(input('Digite um número inteiro '))
num3 = int(input('Digite um número inteiro '))

resultado = num1+num2+num3

print(f'A soma dos três valores é {resultado}')
'''

#Questão 3
'''
num = int(input('Digite um número inteiro '))

ant = num - 1
sucess = num + 1

print(f'O antecessor de {num} é {ant}, e seu sucessor é {sucess}')
'''

#Questão 4
'''
celsius = float(input('Digite a temperatura em Celsius '))

fahrenreit = celsius*(9/5)+32

print(f'A temperatura {celsius} graus Celsius, equivale a {fahrenreit} graus Fahrenreit')
'''

#Questão 5
'''
km_h = float(input('Digite uma velocidade em km/h '))

m_s = km_h/3.6

print(f'A velocidade {km_h} km/h equivale a {m_s:.1f} metros por segundo')
'''

#Questão 6
'''
nota1 = float(input('Digite uma nota '))
nota2 = float(input('Digite outra nota '))
nota3 = float(input('Digite outra nota '))
nota4 = float(input('Digite outra nota '))

media = (nota1+nota2+nota3+nota4)/4

print(f'A média aritmética das notas é {media}')
'''

#Questão 7
'''
real = float(input('Digite o valor em Real Brasileiro '))
dolar = float(input('Digite a cotação atual do dólar '))

cambio = real/dolar
#Formatei em 2 casas decimais para representar os centavos
print(f'R${real} equivale a ${cambio:.2f}')
'''

#Questão 8
'''
raio = int(input('Digite o valor do raio do círculo '))
PI = 3.141592

area_circulo = PI*raio**2
#Não formatei para deixar o valor exato
print(f'A área do círculo é {area_circulo}')

'''

#Questão 9
'''
premio = 780000.00

primeiro = premio * (46/100)
segundo = premio * (32/100)
terceiro = premio - primeiro - segundo

print(f"""
      
O primeiro ganhador levará para casa: R${primeiro}
O segundo ganhador levará para casa: R${segundo}
E o terceiro ganhador levará para casa R${terceiro}      
""")
'''

#Questão 10
'''
num = int(input('Digite um número inteiro '))

if num >0:
    print(f'{num} ao quadrado é {num*num}')
    print(f'A raiz quadrada de {num} é {num**(1/2)}')

else:
    print('DIGITE UM VALOR POSITIVO')
'''

#Questão 11
'''
num = int(input('Digite um número inteiro '))

if num > 0:
    print(f'{num} é positivo e ',end='')
elif num < 0:
    print(f'{num} é negativo e ',end='')

if num %2 == 0 and num != 0:
    print('é par')
elif num %2 != 0:
    print('é ímpar')
else:
    print('Zero é Nulo')
'''

#Questão 12
'''
nota1 = int(input('Digite uma nota '))
nota2 = int(input('Digite a segunda nota '))

if nota1 <0 or nota1 > 10 or nota2 < 0 or nota2 > 10:
    print('DIGITE DUAS NOTAS VÁLIDAS')
else:
    print(f'A média é {(nota1+nota2)/2}')
'''

#Questão 13
'''
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
'''

#Questão 14
'''
nota_lab = float(input('Digite a nota do Laboratório '))
a_semestr = float(input('Digite a nota da Avaliação do Semestre '))
final_exam = float(input('Digite a nota do Exame Final '))

final_lab = nota_lab * 0.2
final_semestr = a_semestr * 0.3
f_final_exam = final_exam * 0.5

final_media = (final_lab+final_semestr+f_final_exam)

if final_media >=0 and final_media <= 2.9:
    print('Reprovado')
elif final_media >=3 and final_media <=4.9:
    print('Recuperação')
else:
    print('Aprovado')
'''

#Questão 15
'''
i = 0
print('Responda: "s" para sim ou "n" para não ')

call_victm = input('Telefonou para a vítima? ')
if call_victm == 's':
    i += 1
stay = input('Esteve no local do crime? ')
if stay == 's':
    i += 1
live = input('Mora perto da vítima? ')
if live == 's':
    i += 1
dues = input('Devia para a vítima? ')
if dues == 's':
    i += 1
job = input('Já trabalhou com a vítima? ')
if job == 's':
    i += 1

if i >= 2:
    if i ==2:
        print('Suspeito')
    if i >= 3 and i <= 4:
        print('Cúmplice')
    if i == 5:
        print('Assasino')
else:
    print('Inocente')
'''

#Questão 16
'''
age = int(input('Digite a idade do trabalhador '))
time_job = int(input('Digite o tempo de serviço '))

if age >= 65 or time_job >= 30:
    print('Pode se aposentar')
elif age >= 60 and time_job >= 25:
    print('Pode se aposentar')
else:
    print('Não pode se aposentar')
'''

#Questão 17
'''
km = float(input('Digite a distância percorrida '))
l = float(input('Digite o gasto de gasolina consumida nessa distância '))

consumo = km/l

if consumo < 8:
    print('Venda o carro!')
elif consumo >=8 and consumo <= 12:
    print('Econômico')
else:
    print('Super econômico')
'''

#Questão 18
'''
#Usando for
for i in range(1,101):
    print(i)

#Usando while

i=1
while i <= 100:
    print(i)
    i+=1
'''

#Questao 19
'''
resultado = 0

for i in range (1,11):
    num = float(input('Digite um valor '))
    resultado += num
#Não foi especificado se era inteiro, logo, coloquei float
print(f'A soma dos valores é {resultado}')
'''

#Questão 20
'''
resultado = 0

for i in range (1,11):
    num = int(input('Digite um valor '))
    resultado += num

print(f'A média é {resultado/10}')
'''

#Questão 21
'''
resultado = 0
positive = 0

for i in range (1,11):
    num = int(input('Digite um valor '))
    if num > 0:
        resultado += num
        positive += 1 

print(f'A média dos números positivos digitados é {resultado/positive}')
'''

#Questão 22
'''
n = int(input('Digite um número '))

for i in range(n+1):
    if i %2 != 0:
        print(i)
'''

#Questão 23
'''
n = int(input('Digite um número inteiro positivo '))

for i in range(n+1):
    print(i)
'''