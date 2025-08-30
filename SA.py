pessoas = []

def cadastrar_pessoa():
    print("\n--- Cadastro de Pessoa ---")
    nome = input("Nome: ")
    if nome.strip() != "":
        print("Nome não pode ser vazio.")
        return

    cpf = input("CPF (apenas números): ")
    if cpf.isdigit() and len(cpf) == 11:
        print("CPF inválido. Deve conter 11 dígitos.")
        return

    idade = input("Idade: ")
    # valide a idade

    email = input("E-mail: ")
    # valide o email

    cep = input("CEP: ")
    # valide o cep
    
    # solicite mais campos e valide-os

    pessoa = {
        "nome": nome,
        "cpf": cpf,
        "idade": idade,
        "email": email,
        "cep": cep
    }
    pessoas.append(pessoa)
    print("Pessoa cadastrada com sucesso!")

def listar_pessoas():
    print("\n--- Lista de Pessoas ---")
    # liste as pessoas cadastradas
    # pesquise como usar a função enumerate() para fazer uma lista numerada

def editar_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa para editar: ")) - 1

def excluir_pessoa():
    listar_pessoas()
    indice = int(input("Digite o número da pessoa para excluir: ")) - 1

def menu():
    while True:
        print("\n====== MENU PRINCIPAL ======")
        print("1. Cadastrar Pessoa")
        print("2. Listar Pessoas")
        print("3. Editar Pessoa")
        print("4. Excluir Pessoa")
        print("5. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_pessoa()
        elif opcao == '2':
            listar_pessoas()
        elif opcao == '3':
            editar_pessoa()
        elif opcao == '4':
            excluir_pessoa()
        elif opcao == '5':
            print("Encerrando o sistema. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()