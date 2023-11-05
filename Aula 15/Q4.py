'''
Escreva um programa para armazenar uma agenda de telefones em um
dicionário. Cada pessoa pode ter um ou mais telefones e a chave do
dicionário é o nome da pessoa. Seu programa deve conter um menu onde
dependendo da entrada do usuário, será possível:
incluirNovoNome – acrescenta um novo nome na agenda, com um ou mais telefones. incluirTelefone – acrescenta um telefone em um nome existente na agenda. Caso o nome
não exista na agenda, você deve perguntar se a pessoa deseja incluí-lo. excluirTelefone – exclui um telefone de uma pessoa que já está na agenda. Se a pessoa tiver
apenas um telefone, ela deve ser excluída da agenda. excluirNome – exclui uma pessoa da agenda. consultarTelefone – retorna os telefones de uma pessoa na agenda.
'''
agenda = {'zezinho': 123}
while True:
    acao = input('O que você gostaria de fazer? *Digite "ajuda" se você não conhece os comandos. \n\n')
    if acao == 'sair': break
    if acao == 'ajuda':
        print('''
              Lista de comandos: 
              incluirNovoNome: Cria um novo nome na Agenda
              incluirTelefone: Inclui um número de Telefone ao contato, podendo existir
              mais de um N°
              excluirTelefone: Exclui um Nº de telefone da pessoa selecionada
              excluirNome: Exclui uma pessoa da agenda
              consultarTelefone: Retornar os telefones de uma pessoa na agenda
              sair: Encerra o Programa\n
              ''')
        
    if acao == 'incluirNovoNome':
        nome = input('Nome: ')
        if nome not in agenda:
            numero = input('Digite o número: ')
            agenda[nome] = [numero]
        else:
            print('Esse nome já consta na agenda')
    if acao == 'incluirTelefone':
        nome = input('De qual contato você gostaria de adicionar um novo numero? \n')
        if nome in agenda:
            numero = input('Digite o número: ')
            agenda[nome].append(numero)
        else:
            print('Esse contato ainda não foi registrado\n')

    if acao == 'excluirTelefone':
        nome = input('De quem você gostaria de excluir um número?\n ')
        if nome in agenda:
            agenda[nome].pop()
            if agenda[nome] == []:
                del agenda[nome]
        else:
            print('Este contato não existe na agenda')

    if acao == 'consultarTelefone':
        print(agenda.get(input('Qual contato você gostaria de consultar? \n'), 'Contato não encontrado na agenda'))

    print()