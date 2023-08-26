num = int(input('Digite um número menor que 1000'))

unidade = num % 10
dezena = (num%100)//10
centena = num //100
plural = 's'

if centena > 1 :
    print(centena,'centena'+plural)
else:
    print(centena,'centena')
if dezena > 1 :
    print(dezena,'dezena'+plural)
else:
    print(dezena,'dezena')
if unidade > 1:
    print(unidade,'unidade'+plural)
else:
    print(unidade,'unidade')
