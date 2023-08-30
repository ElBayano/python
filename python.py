mensagem = 'Bem-vindo ao controle de coladoradores do Samuel Paixão Nascimento'

lista_colaboradores = []
id_global = 0

def print_title(txt):
    metade_txt = len(txt) // 2
    linhas = int(len(mensagem) / 2) - metade_txt - 1
    if len(txt) % 2:
        print('{} {} {}'.format('-' * linhas , txt,'-' * (linhas - 1)))
    else:
        print('{} {} {}'.format('-' * linhas , txt,'-' * linhas))

def cadastrar_colaborador(id_global):
    global lista_colaboradores  
    nome_colaborador = input("Por favor, entre com o nome: ")
    setor_colaborador = input("Por favor, entre com o setor: ")
    pagamento_colaborador = input("Por favor, entre com o pagamento: ")
    dicio = {"id": id_global, "nome": nome_colaborador,"setor": setor_colaborador,
     "pagamento": pagamento_colaborador}
    return lista_colaboradores.append(dicio)

def consultar_colaborador():
    print('Escolha a opção desejada')
    print('1 - Consultar TODOS os colaboradores')
    print('2 - Consultar por ID')
    print('3 - Consultar colaboradores por setor')
    print('4 - Retornar')
    item = lista_colaboradores[:]

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
                    
            if opc == 2:
                try: 
                    id = int(input("\nDigite o Id do colaborador: "))
                except:
                    print("Valor não numérico")
                else:
                    item = item[id - 1]
                    print('-'*20)
                    print('id........: {}'.format(item['id']))
                    print('nome......: {}'.format(item['nome']))
                    print('setor.....: {}'.format(item['setor']))
                    print('pagamento.: {}'.format(item['pagamento']))
                break


            if opc == 3:
                print('2 - Consultar por ID')
            if opc == 4:
                break

            # print('-'*20)
            # print('id........: {}'.format(item['id']))
            # print('nome......: {}'.format(item['nome']))
            # print('setor.....: {}'.format(item['setor']))
            # print('pagamento.: {}'.format(item['pagamento'])) 


def menu():
    while True:
        print('*'*len(mensagem))
        print_title('MENU PRINCIPAL')
        print('\nQual a opção desejada:')
        print('1 - Cadastrar Colaborador \n2 - Consultar Colaborador \n3 - Remover Colaborador \n4 - Encerrar')
        
        try:
            opc = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))

        except ValueError:
            print('Opção inválida. Valor não numerico\n')

        else:
            if opc == 1:
                global id_global
                print('*'*len(mensagem))
                print_title('MENU CADASTRAR COLABORADOR')
                id_global += 1
                cadastrar_colaborador(id_global)
            elif opc == 2:
                print('*'*len(mensagem))
                print_title('MENU CONSULTAR COLABORADOR')
                consultar_colaborador()
            elif opc == 3:
                print('*'*len(mensagem))
                print_title('MENU REMOVER COLABORADOR')
                # remover_colaborador()
            elif opc == 4:
                break
            else: 
                print('Opção inválida')

print(mensagem)


menu()
