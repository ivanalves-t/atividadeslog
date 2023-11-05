lista1 = ['azul','preto','vermelho','branco']
lista2 = ['amarelo','verde',"azul",'vermelho','cinza']
comum = []
only1 = []
only2 = []

for elementos in lista1:
    if elementos not in lista2:
        only1.append(elementos)
    if elementos in lista2:
        comum.append(elementos)
for elementoos in lista2:
    if elementoos not in lista1:
        only2.append(elementoos)

print(str(comum))
print(str(only1))
print(str(only2))
print(str(only2))
print(str(only2),end=str(lista1))