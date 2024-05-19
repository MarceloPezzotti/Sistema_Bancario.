menu = """

[1] Depositar
[2] Sacar
[3] Investimentos
[4] Extrato
[0] Sair

=> """
saldo_investimentos = 0
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    if opcao == "1":
        valor = float(input("Informe o valor do depósito:"))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação falhou o valor informado é invalido.")
    elif opcao == "2":
            valor = float(input("Informe o valor do saque:"))
            
            excedeu_saldo = valor > saldo
            
            excedeu_limite = valor > limite
            
            excedeu_saques = numero_saques >= LIMITE_SAQUES
            
            if excedeu_saldo:
                print("Operação falhou! Você não tem saldo suficiente.")
                
            elif excedeu_limite:
                print("Operaçao falhou! o valor de saque excede o limite.")
                
            elif excedeu_saques:
                print("Operaçao falhou! Número máximo de saques excedido.")
                
            elif valor > 0:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f}\n"
                numero_saques +=1
                
            else:
                print("Operação falhou! o valor informado é invalido.")
               
    elif opcao == "3":
                 valor = float(input("Informe o valor que deseja investir:"))
                 if valor > 0:
                    saldo_investimentos += valor
                    extrato += f"Carteira de investimentos: R$ {valor:.2f}\n"
                
                
                
    elif opcao == "4":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"\nSaldo: R$ {saldo:.2f}" + f"\nSaldo Investimentos: R$ {saldo_investimentos:.2f}")
            
            
            print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.") 
         
     
                             
                
            
            
            
            
            
    
     
