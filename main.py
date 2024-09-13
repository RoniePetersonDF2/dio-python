def depositar(saldo):
    valor = float(input("Informe o valor a ser depositado: R$ "))
    
    if valor > 0:
        saldo += valor

    return saldo

menu = """
Escolha uma das opções abaixo\n
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
"""

LIMITE_SAQUES = 3
saldo = 0
limite_saque = 500
extrato = ""
numero_saques = 0

while True:
        opcao = input(menu).lower()

        if opcao == "d":
            print("Deposito")
            valor = float(input("Informe o valor a ser depositado: R$ "))
            
            if valor > 0:
                saldo += valor
                extrato += f"Deposito: R$ {valor:.2f}\n"
        elif opcao == "s":
            print("Sacar")
            if numero_saques > 2:
                 print("O numero de saques diário foi atingido.")
            else:
                valor = float(input("Informe o valor a ser sacado: R$ "))
                if valor > limite_saque:
                    print("O valor excede o valor de saque.")
                elif valor > saldo:
                    print("Saldo insuficiente para o saque.")
                elif valor <= 0:
                    print("Valor inválido para o saque.")
                else:
                    saldo -=valor
                    numero_saques+=1
                    extrato += f"Saque: R$ {valor:.2f}\n"

        elif opcao == "e":
            print("\n\tExtrato")
            print("Não foram realizadas operações." if not extrato else extrato)
        elif opcao == "q":
             break
        else:
             print("Opção inválida. Tente novamente.")
        
        
