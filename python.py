#Mensagem de boas vindas
mensagem = 'Bem-vindo ao controle de colaboradores do Samuel Paixão Nascimento'

#Criação das variáveis
lista_colaboradores = []
id_global = 0

#Função pra buscar informações por id ou por setor na lista
def buscar_por_info(info, dado, lista, isId = False):
    
    if isId:
        colaborador = lista[dado-1]
        print('-'*20)
        print('id........: {}'.format(colaborador['id']))
        print('nome......: {}'.format(colaborador['nome']))
        print('setor.....: {}'.format(colaborador['setor']))
        print('pagamento.: {}'.format(colaborador['pagamento']))
    else:
        for colaborador in lista:
            if colaborador[info] == dado:
                print('-'*20)
                print('id........: {}'.format(colaborador['id']))
                print('nome......: {}'.format(colaborador['nome']))
                print('setor.....: {}'.format(colaborador['setor']))
                print('pagamento.: {}'.format(colaborador['pagamento']))

#Função para printar titulo centralizado com "*" aos lados
def print_title(txt):
    metade_txt = len(txt) // 2
    linhas = int(len(mensagem) / 2) - metade_txt - 1
    if len(txt) % 2:
        print('{} {} {}'.format('-' * linhas , txt,'-' * (linhas - 1)))
    else:
        print('{} {} {}'.format('-' * linhas , txt,'-' * linhas))


#função para cadastrar colaborador na lista. Recebe com o parâmetro o id global
def cadastrar_colaborador(id):
    global lista_colaboradores  
    nome_colaborador = input("Por favor, entre com o nome: ")
    setor_colaborador = input("Por favor, entre com o setor: ")
    pagamento_colaborador = input("Por favor, entre com o pagamento: ")
    dicio = {"id": id, "nome": nome_colaborador,"setor": setor_colaborador,
     "pagamento": pagamento_colaborador}
    return lista_colaboradores.append(dicio)


# Função para consultar colaborador na lista.
# Chama função buscar_por_info() passando a key a ser buscada e o valor desejado a ser encontrado
# Passa a lista e o tipo da pesquisa. Se é por id ou não
def consultar_colaborador():
    item = lista_colaboradores[:]
    print('Escolha a opção desejada')
    print('1 - Consultar TODOS os colaboradores')
    print('2 - Consultar por ID')
    print('3 - Consultar colaboradores por setor')
    print('4 - Retornar')

    while True:
        try:
            opc = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>>>> '))
        except ValueError:
            print("Opção inválida") 

        else:
            if opc == 1:
                for colaborador in item:
                    print('-'*20)
                    print('id........: {}'.format(colaborador['id']))
                    print('nome......: {}'.format(colaborador['nome']))
                    print('setor.....: {}'.format(colaborador['setor']))
                    print('pagamento.: {}'.format(colaborador['pagamento']))
                break
                    
            elif opc == 2:
                try: 
                    dado = int(input("\nDigite o Id do colaborador: "))
                except:
                    print("Opção inválida. Valor não numérico")
                else:
                    buscar_por_info('id', dado, item, True)
                break


            elif opc == 3:
                dado = input("\nDigite o setor do colaborador: ")
                buscar_por_info('setor', dado, item)
                break
            elif opc == 4:
                break
            else:
                print("Opção inválida.")

# Função para removar um colaborador da lista
def remover_colaborador():
    global lista_colaboradores
    try:
        dado = int(input("\nDigite o Id do colaborador a ser removido: "))
    except:
        print('Valor inválido')
    else:
        indice = dado - 1
        del lista_colaboradores[indice]

#Função para mostrar o menu principal
def menu():
    while True:
        print('*'*len(mensagem))
        print_title('MENU PRINCIPAL')
        print('\nQual a opção desejada:')
        print('1 - Cadastrar Colaborador \n2 - Consultar Colaborador \n3 - Remover Colaborador \n4 - Encerrar')
        
        try:
            opc = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>>>> '))

        except ValueError:
            print('Opção inválida. Valor não numerico\n')

        else:
            if opc == 1:
                global id_global
                id_global += 1
                print('*'*len(mensagem))
                print_title('MENU CADASTRAR COLABORADOR')
                cadastrar_colaborador(id_global)
            elif opc == 2:
                print('*'*len(mensagem))
                print_title('MENU CONSULTAR COLABORADOR')
                consultar_colaborador()
            elif opc == 3:
                print('*'*len(mensagem))
                print_title('MENU REMOVER COLABORADOR')
                remover_colaborador()
            elif opc == 4:
                break
            else: 
                print('Opção inválida')


#Inicio do programa
print(mensagem)

#Chamando menu principal
menu()