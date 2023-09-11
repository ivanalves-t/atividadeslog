'''
Faça uma função que recebe uma string que representa uma cadeia de DNA e gera a
cadeia complementar. A entrada e saída de dados deve ser feita pelo programa
principal.  Exemplo:
 Entrada: AATCTGCAC
 Saída: TTAGACGTG
'''

dna = input('Digite uma fita de DNA ')
dna_t = ''

for i in dna:
    if i == 'A':
        dna_t += 'T'
    elif i == 'T':
        dna_t += 'A'
    elif i == 'C':
        dna_t += 'G'
    elif i == 'G':
        dna_t += 'C'

print(dna_t)