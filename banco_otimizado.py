# ------------------------------
# Banco Winona - Sistema Modular
# ------------------------------

def mostra_linha():
    print("--" * 30)

# Função para criar usuário
def criar_usuario(usuarios):
    cpf = input("Digite o CPF (somente números): ").strip()
    if filtrar_usuario(cpf, usuarios):
        print("Usuário já cadastrado!")
        return
    nome = input("Digite o nome do usuário: ").strip().title()
    usuarios.append({"nome": nome, "cpf": cpf})
    print(f"Usuário {nome} criado com sucesso!")

# Função para filtrar usuário pelo CPF
def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None

# Função para criar conta
def criar_conta(contas, usuarios):
    cpf = input("Digite o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({"numero": numero_conta, "usuario": usuario, "saldo": 0.0, "extrato": []})
        print(f"Conta {numero_conta} criada para {usuario['nome']}.")
    else:
        print("Usuário não encontrado. Crie o usuário antes de criar a conta.")

# Listar contas
def listar_contas(contas):
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    for conta in contas:
        print(f"Conta {conta['numero']}: {conta['usuario']['nome']} - Saldo: R$ {conta['saldo']:.2f}")

# Função para depositar
def depositar(conta):
    valor = float(input("Digite o valor do depósito: "))
    if valor > 0:
        conta['saldo'] += valor
        conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

# Função para sacar
def sacar(conta, limite_saques=3, limite_valor=500):
    if limite_saques <= 0:
        print("Número de saques excedido.")
        return limite_saques
    valor = float(input("Digite o valor do saque: "))
    if valor <= conta['saldo']:
        conta['saldo'] -= valor
        conta['extrato'].append(f"Saque: R$ {valor:.2f}")
        print(f"Saque de R$ {valor:.2f} realizado. Saldo atual: R$ {conta['saldo']:.2f}")
    elif valor <= conta['saldo'] + limite_valor:
        limite_usado = valor - conta['saldo']
        conta['saldo'] = 0
        limite_valor -= limite_usado
        conta['extrato'].append(f"Saque com limite: R$ {valor:.2f}")
        print(f"Saque realizado usando R$ {limite_usado:.2f} do limite.")
        print(f"Limite restante: R$ {limite_valor:.2f}")
    else:
        print("Saldo e limite insuficientes.")
    return limite_saques - 1

# Função para exibir extrato
def exibir_extrato(conta):
    mostra_linha()
    print(f"EXTRATO - Conta {conta['numero']} ({conta['usuario']['nome']})")
    if conta['extrato']:
        for item in conta['extrato']:
            print(item)
    else:
        print("Não foram realizadas movimentações.")
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    mostra_linha()

# Menu principal
def menu():
    print("\nBem-vindo ao Banco Winona")
    mostra_linha()
    print("[1] Criar Usuário")
    print("[2] Criar Conta")
    print("[3] Listar Contas")
    print("[4] Depositar")
    print("[5] Sacar")
    print("[6] Extrato")
    print("[0] Sair")
    mostra_linha()
    return input("Escolha uma opção: ").strip()

# -----------------------------
# Programa Principal
# -----------------------------
usuarios = []
contas = []
limite_saques = 3

while True:
    opcao = menu()

    if opcao == "0":
        print("Saindo do sistema...")
        break
    elif opcao == "1":
        criar_usuario(usuarios)
    elif opcao == "2":
        criar_conta(contas, usuarios)
    elif opcao == "3":
        listar_contas(contas)
    elif opcao == "4":
        numero = int(input("Digite o número da conta: "))
        conta = next((c for c in contas if c["numero"] == numero), None)
        if conta:
            depositar(conta)
        else:
            print("Conta não encontrada.")
    elif opcao == "5":
        numero = int(input("Digite o número da conta: "))
        conta = next((c for c in contas if c["numero"] == numero), None)
        if conta:
            limite_saques = sacar(conta, limite_saques)
        else:
            print("Conta não encontrada.")
    elif opcao == "6":
        numero = int(input("Digite o número da conta: "))
        conta = next((c for c in contas if c["numero"] == numero), None)
        if conta:
            exibir_extrato(conta)
        else:
            print("Conta não encontrada.")
    else:
        print("Opção inválida! Tente novamente.")
