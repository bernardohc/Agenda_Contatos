agenda = {}

def mostrar_contatos():
    if agenda:
        for contato in agenda:
            buscar_contato(contato)
    else:
        print(">> Agenda vazia <<")
        print()


def buscar_contato(contato):
    try:
        print("Nome:", contato)
        print("Telefone", agenda[contato]['telefone'])
        print("E-mail", agenda[contato]['email'])
        print("Endereço", agenda[contato]['endereco'])
        print()
    except KeyError:
        print(">> Contato inexistente <<")
    except Exception as error:
        print(">> Um erro inexperado ocorreu - 01 <<")
        print(error)


def ler_detalhes():
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    endereco = input("Digite o endereço: ")
    return telefone, email, endereco


def incluir_editar_contato(contato, telefone, email, endereco):
    agenda[contato] = {
        "telefone": telefone,
        "email": email,
        "endereco": endereco,
    }
    salvar()
    print("<< Contato {} adicionado/editado com sucesso >>".format(contato))
    print()


def excluir_contato(contato):
    try:
        agenda.pop(contato)
        salvar()
        print("<< Contato {} excluido com sucesso >>".format(contato))
        print()
    except KeyError:
        print(">> Contato inexistente <<")
    except Exception as error:
        print(">> Um erro inexperado ocorreu - 02 <<")
        print(error)


def exportar_contatos(file_name):
    try:
        with open(file_name, "w") as arquivo:
            for contato in agenda:
                telefone = agenda[contato]["telefone"]
                email = agenda[contato]["email"]
                endereco = agenda[contato]["endereco"]
                arquivo.write("{};{};{};{}\n".format(contato, telefone, email, endereco))
        print(">> Agenda exportada com sucesso <<")
    except Exception as error:
        print(">> Algum erro ocorreu ao exportar os cantatos <<")
        print(error)


def importar_contatos(file_name):
    try:
        with open(file_name, "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(";")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]
                incluir_editar_contato(nome, telefone, email, endereco)
    except FileNotFoundError:
        print(">> Arquivo não econtrado <<")
    except Exception as error:
        print(">> Algum erro inesperado ocorreu - 03 <<")
        print(error)

def salvar():
    exportar_contatos("database.csv")

def carregar():
    try:
        with open("database.csv", "r") as arquivo:
            linhas = arquivo.readlines()
            for linha in linhas:
                detalhes = linha.strip().split(";")
                nome = detalhes[0]
                telefone = detalhes[1]
                email = detalhes[2]
                endereco = detalhes[3]

                agenda[nome] = {
                    "telefone": telefone,
                    "email": email,
                    "endereco": endereco,
                }
        print(">> Database importado com sucesso! <<")
        print(">> {} Contatos carregados".format(len(agenda)))
    except FileNotFoundError:
        print(">> Arquivo não econtrado <<")
    except Exception as error:
        print(">> Algum erro inesperado ocorreu - 04 <<")
        print(error)

def imprimir_menu():
    print("----------------------------")
    print("1 - Mostrar todos contatos")
    print("2 - Buscar contato")
    print("3 - Incluir contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Exportar contatos CSV")
    print("7 - Importar contatos CSV")
    print("0 - Fechar agenda")
    print("----------------------------")


print()

# Inicio Programa

carregar()

while True:
    imprimir_menu()
    print()
    opcao = input("Escolha uma opção: ")
    print()

    if opcao == "1":
        mostrar_contatos()
    elif opcao == "2":
        contato = input("Digite o nome do contato: ")
        print()
        buscar_contato(contato)
    elif opcao == "3":
        contato = input("Digite o nome do contato: ")
        try:
            agenda[contato]
            print(">> Contato já existente! <<")
        except KeyError:
            telefone, email, endereco = ler_detalhes()4
            incluir_editar_contato(contato, telefone, email, endereco)
    elif opcao == "4":
        contato = input("Digite o nome do contato: ", )
        try:
            agenda[contato]
            print(">> Editando contato <<", contato)
            telefone, email, endereco = ler_detalhes()
            incluir_editar_contato(contato, telefone, email, endereco)
        except KeyError:
            print(">> Contato inexistente <<")
    elif opcao == "5":
        contato = input("Digite o nome de contato: ")
        excluir_contato(contato)
    elif opcao == "6":
        file_name = input(">> Digite o nome do arquivo a ser exportado << ")
        exportar_contatos(file_name)
    elif opcao == "7":
        file_name = input(">> Digite o nome do arquivo a ser importado << ")
        importar_contatos(file_name)
    elif opcao == "0":
        print(">> Agenda finalizado <<")
        break
    else:
        print("Opção inválida")


