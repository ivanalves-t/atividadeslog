'''
Faça um programa que solicite ao usuário uma string e modifique a string
para que todos os caracteres fiquem em maiúsculas. Obs: Não utilize a função upper(). Utilize a tabela ASCII.
'''
str1 = input('Digite a palavra')
str2 = ''
str3 = ''
for i in str1:
    str2 = ord(i) - 32
    str3 += chr(str2)

print(str3)
