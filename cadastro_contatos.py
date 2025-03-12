import copy

lista_contatos = []
id_global = 100200 

def cadastrar_contato(id):
    print('-' * 59)
    print('------------------MENU CADASTRAR CONTATO-------------------')
    print(f'Id do contato:{id}')
    nome = input('Informe o nome do contato: ')
    atividade = input('Informe a atividade do contato: ')
    telefone = input('Informe o telefone do contato: ')
    print()
    
    # Dicionário 
    contato = {
        'id': id,
        'nome': nome.lower(),
        'atividade': atividade.lower(),
        'telefone': telefone
    }
    
    # Copiando o dicionário para lista de contatos
    lista_contatos.append(copy.deepcopy(contato))
    print('Contato cadastrado com sucesso!')
    print()

def consultar_contatos():
    while True:
        print('-' * 59)
        print('-----------------MENU CONSULTAR CONTATOS-------------------')
        print('Escolha a opção desejada:')
        print('1 - Consultar todos os Contatos')
        print('2 - Consultar Contato por id')
        print('3 - Consultar Contato(s) por Atividade')
        print('4 - Retornar')
        print()
        
        opcao = input('>>')
        
        if opcao == '1':
            print('Lista de todos os contatos:')
            for contato in lista_contatos:
                print(contato)
      
        elif opcao == '2':
            id_procurado = input('Informe o id do contato: ')
            encontrado = False
            for contato in lista_contatos:
                if str(contato['id']) == id_procurado:
                    print(contato)
                    encontrado = True
                    break
            if not encontrado:
                print('Contato não encontrado.')

        elif opcao == '3':
            atividade_procurada = input('Informe a atividade do contato: ').lower()
            encontrados = [contato for contato in lista_contatos if contato['atividade'] == atividade_procurada]
            if encontrados:
                for contato in encontrados:
                    print(contato)
            else:
                print('Nenhum contato encontrado com essa atividade.')

        elif opcao == '4':
            return

        else:
            print('Opção inválida!')

def remover_contato():
    while True:
        print('-' * 59)
        print('-------------------MENU REMOVER CONTATO--------------------')
        id_remover = input('Informe o id do contato a ser removido: ')
        for contato in lista_contatos:
            if str(contato['id']) == id_remover:
                lista_contatos.remove(contato)
                print('Contato removido com sucesso!')
                return
        print('Id inválido! Tente novamente.')

#MAIN

while True:
    print('-' * 59)
    print('----------------------MENU PRINCIPAL-----------------------')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Contato')
    print('2 - Consultar Contato(s)')
    print('3 - Remover Contato')
    print('4 - Sair')
    print()
    
    opcao = input('>>')
    
    if opcao == '1':
        cadastrar_contato(id_global)
        id_global += 1
        
    elif opcao == '2':
        consultar_contatos()
        
    elif opcao == '3':
        remover_contato()
        
    elif opcao == '4':
        print('Encerrando programa...')
        break
    
    else:
        print('Opção inválida!')





