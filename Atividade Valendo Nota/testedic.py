# # # A = float(input())
# # # B = float(input())
# # # C = float(input())

# # # media = ((A*2)+(B*3)+(C*5))/(2+3+5)

# # # print(f'MEDIA = {media:.1f}')

# # A = int(input())
# # B = int(input())
# # C = int(input())
# # D = int(input())

# # dif = (A * B - C * D)

# # print(f'DIFERENCA = {dif}')

# # number = input()
# # worked_hours = int(input())
# # payment = float(input())

# # sal = worked_hours * payment

# # print(f'NUMBER = {number}')
# # print(f'SALARY = U$ {sal:.2f}')

# # name = input()
# # salary = float(input())
# # solds = float(input())

# # total = salary + solds*(15/100)

# # print(f'TOTAL = R$ {total:.2f}')

# p1 = input()
# p2 = input()
# codigo1,numero1,valor1 = p1.split(' ')
# codigo2,numero2,valor2 = p2.split(' ')

# valor = float(numero1)*float(valor1)+float(numero2)*float(valor2)

# print(f'VALOR A PAGAR: R$ {valor:.2f}')

# r = int(input())
# vol = (4/3)*3.14159*r**3

# print(f'VOLUME = {vol:.3f}')

# valores = input()
# A,B,C = map(float, valores.split(' '))

# print(f'TRIANGULO: {A * C /2:.3f}')
# print(f'CIRCULO: {3.14159 * C ** 2:.3f}')
# print(f'TRAPEZIO: {C / 2 * (A + B):.3f}')
# print(f'QUADRADO: {B * B:.3f}')
# print(f'RETANGULO: {A * B:.3f}')

# print(f'''
# TRIANGULO: {t:.3f}
# CIRCULO: {cir:.3f}
# TRAPEZIO: {tra:.3f}
# QUADRADO: {q:.3f}
# RETANGULO: {r:.3f}
# ''')

# valores = input()
# A,B,C = map(int, valores.split(' '))
# biggerAB = (A+B+abs(A-B))/2
# if biggerAB > C:
#     print(f'{biggerAB:.0f} eh o maior')
# else:
#     print(f'{C:.0f} eh o maior')

# x = int(input())
# y = float(input())

# medium = x/y

# print(f'{medium:.3f} km/l')

# a = int(input())
# print(f'{a*2} minutos')

# t = int(input())
# v = int(input())
# l = (v*t)/12
# print(f'{l:.3f}')
# num = int(input())
# if num > 0 and num < 1000000:
#     notas = [100,50,20,10,5,2,1]
#     for nota in notas:
#         print(f'{num//nota} nota(s) de R$ {nota},00')
#         num %= nota

# t = int(input())
# time = [3600,60,1]
# luriu = []
# for tempo in time:
#     luriu.append(t//tempo)
#     t %= tempo

# print(f'{luriu[0]}:{luriu[1]}:{luriu[2]}')
# dias = int(input())
# days = [365,30,1]
# diaa = []

# for dia in days:
#     diaa.append(dias//dia)
#     dias %= dia

# print(f'{diaa[0]} ano(s)')
# print(f'{diaa[1]} mes(es)')
# print(f'{diaa[2]} dia(s)')

# num = float(input())
# if num > 0 and num < 1000000:
#     moedas = [1,0.5,0.25,0.1,0.05,0.01]
#     notas = [100,50,20,10,5,2]
#     print('NOTAS:')
#     for nota in notas:
#         print(f'{num//nota:.0f} nota(s) de R$ {nota:.2f}')
#         num %= nota
#     print('MOEDAS:')
#     for moeda in moedas:
#         print(f'{num//moeda:.0f} moeda(s) de R$ {moeda:.2f}')
#         num %= moeda

# num = float(input())
# if num > 0 and num < 1000000:
#     dinheiro = [100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]

# for money in dinheiro:
#     if money == dinheiro[0]:
#         print('NOTAS:')
#     if money > dinheiro[6]:
#         print(f'{int(num//money)} nota(s) de R$ {money:.2f}')
#     if money == dinheiro[6]:
#         print('MOEDAS:')
#     if money < 2:
#         print(f'{int(num//money)} moeda(s) de R$ {money:.2f}')
#     num %= money


# a,b,c,d = map(int, input().split(' '))

# cEd = c + d
# aEb = a + b

# if b > c and d > a and cEd > aEb and c > 0 and d > 0 and a %2 == 0:
#     print('Valores aceitos')
# else:
#     print('Valores nao aceitos')

# a,b,c = map(float, input().split(' '))

# delta = b*b-4*a*c

# raiz = delta**(0.5)

# print(raiz)
# # if a == 0:
# #     print('Impossivel calcular')
# else:
#     print(delta)

# for i in range(1,101):
#     if i %2 == 0:
#         print(i)

# mes = {
# '1' : "January",
# '2' : 'February',
# "3" : 'March',
# '4' : "April",
# "5" : 'May',
# "6" : 'June',
# '7' : 'July',
# '8' : 'August',
# '9' : 'September',
# '10': 'October',
# '11': 'November',
# '12': 'December'
# }

# month = input()

# print(f'{mes[month]}')

# p = 0
# for i in range(6):
#     v = float(input())
#     if v > 0:
#         p +=1

# print(f'{p} valores positivos')

# num = int(input())
# if num %2 == 0:
#     num += 1
# for i in range(6):
#     print(num)
#     num +=2

# ddd = {
# '61' : 'Brasilia',
# '71' : 'Salvador',
# '11' : 'Sao Paulo',
# '21' : 'Rio de Janeiro',
# '32' : 'Juiz de Fora',
# '19' : 'Campinas',
# '27' : 'Vitoria',
# '31' : 'Belo Horizonte'
# }

# dididi = input()

# if dididi not in ddd:
#     print('DDD nao cadastrado')
# else:
#     print(f'{ddd[dididi]}')
# positive = 0
# media = 0

# for i in range(6):
#     num = float(input())
#     if num > 0:
#         media += num
#         positive += 1

# media /= positive

# print(f'{positive} valores positivos')
# print(f'{media:.1f}')
# j = 0

# for i in range (5):
#     num = int(input())
#     if num %2 == 0:
#         j += 1

# print(f'{j} valores pares')

# a,b,c = map(float, input().split(' '))

# delta = b*b-4*a*c

# if a == 0 or delta < 0:
#     print('Impossivel calcular')
# else:
#     x1 = ((-b)+delta**0.5)/(2*a)
#     x2 = ((-b)-delta**0.5)/(2*a)
#     print(f'R1 = {x1:.5f}')
#     print(f'R2 = {x2:.5f}')

# num = float(input())

# if num >= 0 and num <= 25:
#     print('Intervalo [0,25]')
# elif num > 25 and num <= 50:
#     print('Intervalo (25,50]')
# elif num > 50 and num <=75:
#     print('Intervalo (50,75]')
# elif num > 75 and num <=100:
#     print('Intervalo (75,100]')
# else:
#     print('Fora de intervalo')

# menu = {
# 1 : 4.00,
# 2 : 4.50,
# 3 : 5.00,
# 4 : 2.00,
# 5 : 1.50
# }

# c,q = map(int, input().split(' '))

# total = menu[c]*q

# print(f'Total: R$ {total:.2f}')

# a,b,c,d = map(float, input().split(' '))

# media = (a*2+b*3+c*4+d*1)/(2+3+4+1)
# print(f'Media: {media:.1f}')

# if media >= 5 and media <= 6.9:
#     print('Aluno em exame.')
#     exame = float(input())
#     print(f'Nota do exame: {exame:.1f}')
#     recuperacao = (media+exame)/2
#     if recuperacao >=5:
#         print('Aluno aprovado.')
#         print(f'Media final: {recuperacao:.1f}')
#     else:
#         print('Aluno reprovado.')
# elif media < 5:
#     print('Aluno reprovado.')
# else:
#     print('Aluno aprovado.')

# x,y = map(float, input().split(' '))

# if x < 0 and y < 0:
#     print('Q3')
# elif x > 0 and y > 0:
#     print('Q1')
# elif x < 0 and y > 0:
#     print('Q2')
# elif x > 0 and y < 0:
#     print('Q4')
# if x == 0 and y != 0:
#     print('Eixo Y')
# if y == 0 and x != 0:
#     print('Eixo X')
# if x == 0 and y == 0:
#     print('Origem')

# values = input().split(' ')
# values = list(map(int , values))
# i,j,k = values

# values.sort()
# x,y,z = values

# print(f'{x}\n{y}\n{z}\n')
# print(f'{i}\n{j}\n{k}')

# Value = input().split(' ')
# Value = list(map(float , Value))
# a,b,c = Value

# if a+b > c and b+c > a and a+c > b:
#     perimetro = a+b+c
#     print(f'Perimetro = {perimetro:.1f}')
# else:
#     area = (c/2)*(a+b)
#     print(f'Area = {area:.1f}')

# num = input().split()
# num = list(map(int, num))
# a,b = num

# if a%b == 0 or b%a ==0:
#     print('Sao Multiplos')
# else:
#     print('Nao sao Multiplos')
# num = input().split()
# num = list(map(float , num))
# a,b,c = num

# if a+b <= c or b+c <= a or a+c <= b or a < 0 or b < 0 or c < 0:
#     print('NAO FORMA TRIANGULO')
# else:
#     if c**2 == b**2+a**2:
#         print('TRIANGULO RETANGULO')
#     if (c**2) > (b**2+a**2):
#         print('TRIANGULO OBTUSANGULO')
#     if (c**2) < (b**2+a**2):
#         print('TRIANGULO ACUTANGULO')
#     if a == b == c:
#         print('TRIANGULO EQUILATERO')
#     if a == b and a != c or b == c and b != a or c == a and c != b:
#         print('TRIANGULO ISOSCELES')

# time = input().split()
# time = list(map(int , time))
# a,b = time

# if a>=b:
#     h = 24 - a + b
#     if h >= 1 and h <=24:print(f'O JOGO DUROU {h} HORA(S)')
# else:
#     h = abs(a-b)
#     if h >= 1 and h <=24:print(f'O JOGO DUROU {h} HORA(S)')