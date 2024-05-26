menu = """

[d] Depósito
[s] Saque
[e] Extrato
[f] Fim

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

while True:

    letra = input(menu)

    if letra == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! Valor informado inválido.")

    elif letra == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            print("Operação falhou! Sem saldo.")

        elif excedeu_limite:
            print("Operação falhou! Valor excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! Valor inválido.")

    elif letra == "e":
        print("\n***** EXTRATO ****")
        print("Sem movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("*********************")

    elif letra == "f":
        break

    else:
        print("Operação inválida, informe a opção desejada.")