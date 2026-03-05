from modulo import *
# Sistema Financeiro Pessoal

while True:
    print("\nMENU FINANCEIRO")
    print("1 - Registrar receita")
    print("2 - Registrar despesa")
    print("3 - Ver saldo")
    print("4 - Mostrar relatório")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    match opcao:
        case "1":
            registrar_receita()

        case "2":
            registrar_despesa()

        case "3":
            saldo = calcular_saldo()
            print(f"Saldo atual: R$ {saldo:.2f}")

        case "4":
            mostrar_relatorio()

        case "5":
            print("Encerrando o sistema...")
            break

        case _:
            print("Opção inválida!")
