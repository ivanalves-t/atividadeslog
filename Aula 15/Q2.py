'''
Crie um dicionário vazio semana = {} e o complete com uma chave para cada
dia da semana, tendo como seu valor uma lista com as aulas que você tem
nesse dia (sábado e domingo recebem listas vazias, ou você tem aula?)
'''

semana = {}
semana['Segunda - Feira'] = 'Duas aulas de Marcelo (Lógica Matemática) e Duas aulas de Xerolaine (Fundamentos da Matemática)'
semana['Terça - Feira'] = 'Duas aulas de Tabica (Informática) e Duas aulas de Xerolaine (Fundamentos da Matemática)'
semana['Quarta - Feira'] = 'Duas aulas de Leonardo (Inovação e Startups) e Duas aulas de Padilha (Inglês)'
semana['Quinta - Feira'] = 'Quatro aulas de Lógica de Programação'
semana['Sexta - Feira'] = 'Quatro aulas de Lógica de Programação'
semana['Sábado'] = []
semana['Domingo'] = []

print(semana[input('Digite o dia da Semana para saber o Horário das aulas: ')])
print()