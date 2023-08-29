mensagem = 'Bem-vindo ao controle de coladoradores do Samuel Paixão Nascimento'
print(mensagem)
print('*'*len(mensagem))

def print_title(txt):
    metade_txt = len(txt) // 2
    print('{} {} {}'.format(metade_txt - 1, txt, metade_txt - 1))

lista_colaboradores = []
id_global = 0

def menu():
    while True:
        print('\nQual a opção desejada:')
        print('1 - Cadastrar Colaborador \n2 - Consultar Colaborador \n3 - Remover Colaborador \n4 -Encerrar')

        try:
            opc = int(input('>>>>>>>>>>>>>>>>>>>>>>>>>>>>'))

        except ValueError:
            print('Opção inválida. Valor não numerico\n')

        else:
            if opc == 1:
                print("Ok")
            elif opc == 2:
                print("2")
            elif opc == 3:
                print("3")
            elif opc == 4:
                print("4")
            else: 
                print('Opção inválida')

menu()