'''
nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?). 3. Crie um dicionário vazio filmes = {}. Utilize o nome de um filme como chave. E, como valor, outro dicionário contendo o vilão e o ano em que o filme foi
lançado. Preencha 5 filmes e acesse os dados do dicionários.
'''

Filmes = {
'Cidade de Deus': 'Vilão: Polícia, Ano: 2002',
'Harry Potter': 'Vilão: Voldemort, Ano: 2007',
'Homem Aranha': 'Vilão: Duende Verde, Ano: 2004',
'Humble': 'Vilão: Zezim do arroz, Ano: 2023',
'Rambo': 'Vilão: Soviéticos, Ano: 199x'
}

print(Filmes[input('Digite o Nome do filme:')])