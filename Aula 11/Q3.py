'''
Faça um programa que solicite uma string ao usuário e em
seguida a imprima em formato de escada.
'''

str1 = input('Digite seu nome ')

for i in range(len(str1)+1):
    print(str1[:i])
    
'''
print(str1[:i])
É Como se fosse:
print(i)
i += i
'''
