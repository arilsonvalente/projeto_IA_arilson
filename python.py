alunos = []

while True:

    print("\n===== SISTEMA DE ALUNOS =====")
    print("1 - Cadastrar aluno")
    print("2 - Listar alunos")
    print("3 - Pesquisar aluno")
    print("4 - Remover aluno")
    print("5 - Quantidade de alunos")
    print("6 - Organizar alunos")
    print("7 - Sair")

    opcao = input("\nEscolha uma opção: ")


    if opcao == "1":

        nome = input("Digite o nome do aluno: ")

        alunos.append(nome)

        print(f"Aluno '{nome}' cadastrado com sucesso!")

    
    elif opcao == "2":

        if len(alunos) == 0:
            print("\nNenhum aluno cadastrado.")
        else:
            print("\n===== LISTA DE ALUNOS =====")

            for numero, aluno in enumerate(alunos, start=1):
                print(f"{numero} - {aluno}")

    # 3 - PESQUISAR ALUNO
    elif opcao == "3":

        pesquisa = input("Digite o nome do aluno que deseja pesquisar: ")

        encontrados = []

        for aluno in alunos:
            if pesquisa.lower() in aluno.lower():
                encontrados.append(aluno)

        if len(encontrados) == 0:
            print("\nAluno não encontrado.")
        else:
            print("\n===== ALUNOS ENCONTRADOS =====")

            for aluno in encontrados:
                print(f"- {aluno}")

    # 4 - REMOVER ALUNO
    elif opcao == "4":

        if len(alunos) == 0:
            print("\nNenhum aluno cadastrado.")
        else:

            print("\n===== LISTA DE ALUNOS =====")

            for numero, aluno in enumerate(alunos, start=1):
                print(f"{numero} - {aluno}")

            try:
                numero = int(input("\nDigite o número do aluno que deseja remover: "))

                if 1 <= numero <= len(alunos):

                    removido = alunos.pop(numero - 1)

                    print(f"\nAluno '{removido}' removido com sucesso!")

                else:
                    print("\nNúmero de aluno inválido.")

            except ValueError:
                print("\nDigite apenas números.")

    # 5 - QUANTIDADE DE ALUNOS
    elif opcao == "5":

        quantidade = len(alunos)

        print(f"\nQuantidade de alunos cadastrados: {quantidade}")

    # 6 - ORGANIZAR ALUNOS
    elif opcao == "6":

        if len(alunos) == 0:
            print("\nNenhum aluno cadastrado.")
        else:

            alunos.sort()

            print("\nAlunos organizados em ordem alfabética!")

            print("\n===== ALUNOS ORGANIZADOS =====")

            for numero, aluno in enumerate(alunos, start=1):
                print(f"{numero} - {aluno}")

    # 7 - SAIR
    elif opcao == "7":

        print("\nSistema encerrado. Até logo!")
        break

    # OPÇÃO INVÁLIDA
    else:

        print("\nOpção inválida!")
        print("Escolha uma opção entre 1 e 7.")