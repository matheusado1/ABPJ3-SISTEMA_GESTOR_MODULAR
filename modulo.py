receitas = []
despesas = []

def registrar_receita():
    valor = float(input("Digite o valor da receita: "))
    receitas.append(valor)
    print("Receita adicionada com sucesso!")

def registrar_despesa():
    valor = float(input("Digite o valor da despesa: "))
    despesas.append(valor)
    print("Despesa adicionada com sucesso!")

def calcular_saldo():
    total_receitas = sum(receitas)
    total_despesas = sum(despesas)
    saldo = total_receitas - total_despesas
    return saldo

def mostrar_relatorio():
    print("\nRELATÓRIO FINANCEIRO")

    print("\nReceitas registradas:")
    for r in receitas:
        print(f"R$ {r:.2f}")

    print("\nDespesas registradas:")
    for d in despesas:
        print(f"R$ {d:.2f}")

    print(f"\nTotal de receitas: R$ {sum(receitas):.2f}")
    print(f"Total de despesas: R$ {sum(despesas):.2f}")
    print(f"Saldo final: R$ {calcular_saldo():.2f}")

