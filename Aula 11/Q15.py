'''
Faça um programa em que troque todas as ocorrencias de uma letra L1 pela
letra L2 e da L2 pela L1 em uma string. A string e as letras L1 e L2 devem ser
fornecidas pelo usuario. Obs: Não utilize a função replace().
'''
str1 = input('Write a word: ')
swap_l1 = input('Which letter do you want to swap? ')
swap_l2 = input('For which letter do you want to swap? ')
to_swap = ''

for i in str1:
    if i != swap_l1:
        to_swap += i
    elif i == swap_l1:
        to_swap += swap_l2

print(to_swap)
