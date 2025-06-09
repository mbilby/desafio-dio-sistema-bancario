from transacao import deposito, registrar_extrato, saque
from utils import verificar_execedeu_saldo, verificar_limite, verificar_numero_saques
from menu import menu

menu = menu()

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:

            saldo = deposito(valor, saldo)
            extrato = registrar_extrato(valor, extrato)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("O valor do depósito deve ser maior que 0 (Zero).")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = verificar_execedeu_saldo(valor, saldo)

        excedeu_limite = verificar_limite(valor, limite)

        excedeu_saques = verificar_numero_saques(numero_saques, LIMITE_SAQUES)

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:

            saldo = saque(valor, saldo)
            extrato = registrar_extrato(valor, extrato)
            numero_saques += 1
            excedeu_saques = verificar_numero_saques(numero_saques, LIMITE_SAQUES)
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")