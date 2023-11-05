'''
Contagem de ocorrências: Dado um texto armazenado em uma string, crie
um programa que conte a quantidade de ocorrências de cada palavra e
retorne uma tupla contendo a palavra e o número de ocorrências.  Exemplo: Para o texto: "A casa é bonita, a casa é azul",
 a saída seria (('A',1), ('casa', 2), ('é', 2), ('bonita,', 1), ('a', 1), ('azul', 1)).
'''
texto = list(map(str, input('Digite o texto: ').split(" ")))

tupla = [(carac, texto.count(carac)) for carac in texto]
tupla = tuple(set(tupla))

print(tupla)