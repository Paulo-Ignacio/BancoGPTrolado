# Dicionário para armazenar usuários
usuarios = {}

# Dicionário para armazenar contas correntes
contas = {}

def cadastrar_usuario(nome, cpf):
    if cpf in usuarios:
        print("Usuário já cadastrado.")
    else:
        usuarios[cpf] = {"nome": nome, "cpf": cpf}
        contas[cpf] = {"saldo": 0.0, "extrato": []}
        print(f"Usuário {nome} cadastrado com sucesso.")

def depositar(cpf, valor):
    if cpf in contas:
        if valor > 0:
            contas[cpf]["saldo"] += valor
            contas[cpf]["extrato"].append(f"Depósito: +R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito deve ser positivo.")
    else:
        print("Usuário não encontrado.")

def sacar(cpf, valor):
    if cpf in contas:
        if valor <= contas[cpf]["saldo"]:
            contas[cpf]["saldo"] -= valor
            contas[cpf]["extrato"].append(f"Saque: -R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Saldo insuficiente para realizar o saque.")
    else:
        print("Usuário não encontrado.")

def transferir(cpf_origem, cpf_destino, valor):
    if cpf_origem in contas and cpf_destino in contas:
        if valor > contas[cpf_origem]["saldo"]:
            print("Saldo insuficiente para transferência.")
        else:
            contas[cpf_origem]["saldo"] -= valor
            contas[cpf_destino]["saldo"] += valor
            contas[cpf_origem]["extrato"].append(f"Transferência enviada: -R${valor:.2f} para {usuarios[cpf_destino]['nome']}")
            contas[cpf_destino]["extrato"].append(f"Transferência recebida: +R${valor:.2f} de {usuarios[cpf_origem]['nome']}")
    else:
        print("Usuário de origem ou destino não encontrado.")

def gerar_extrato(cpf):
    if cpf in contas:
        print(f"Extrato da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}):")
        for item in contas[cpf]["extrato"]:
            print(item)
        print(f"Saldo atual: R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def editar_usuario(cpf):
    if cpf in usuarios:
        novo_nome = input("Digite o novo nome: ").strip()
        usuarios[cpf]['nome'] = novo_nome
        print(f"Dados do usuário {cpf} atualizados para: {usuarios[cpf]}")
    else:
        print("Usuário não encontrado.")

def fechar_conta(cpf):
    if cpf in usuarios:
        del usuarios[cpf]
        del contas[cpf]
        print(f"Conta do usuário com CPF {cpf} fechada com sucesso.")
    else:
        print("Usuário não encontrado.")

def consultar_saldo(cpf):
    if cpf in contas:
        print(f"Saldo atual da conta de {usuarios[cpf]['nome']} (CPF: {usuarios[cpf]['cpf']}): R${contas[cpf]['saldo']:.2f}")
    else:
        print("Usuário não encontrado.")

def menu():
    while True:
        print("\n=== Sistema Bancário ===")
        print("[ 1 ] Cadastrar usuário")
        print("[ 2 ] Consultar saldo")
        print("[ 3 ] Depositar")
        print("[ 4 ] Sacar")
        print("[ 5 ] Transferir")
        print("[ 6 ] Gerar extrato")
        print("[ 7 ] Editar usuário")
        print("[ 8 ] Fechar conta")
        print("[ 9 ] Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Digite o nome: ").strip()
            cpf = input("Digite o CPF: ").strip()
            cadastrar_usuario(nome, cpf)
        elif escolha == "2":
            cpf = input("Digite o CPF: ").strip()
            consultar_saldo(cpf)
        elif escolha == "3":
            cpf = input("Digite o CPF: ").strip()
            valor = float(input("Digite o valor a depositar: "))
            depositar(cpf, valor)
        elif escolha == "4":
            cpf = input("Digite o CPF: ").strip()
            valor = float(input("Digite o valor a sacar: "))
            sacar(cpf, valor)
        elif escolha == "5":
            cpf_origem = input("Digite o CPF de origem: ").strip()
            cpf_destino = input("Digite o CPF de destino: ").strip()
            valor = float(input("Digite o valor da transferência: ").strip())
            transferir(cpf_origem, cpf_destino, valor)
        elif escolha == "6": 
            cpf = input("Digite o CPF: ").strip()
            gerar_extrato(cpf)
        elif escolha == "7":
            cpf = input("Digite o CPF: ").strip()
            editar_usuario(cpf)
        elif escolha == "8":
            cpf = input("Digite o CPF: ").strip()
            fechar_conta(cpf)
        elif escolha == "9":
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
menu()