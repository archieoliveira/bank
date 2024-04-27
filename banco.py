from datetime import datetime

limite_saque = deposito = saque = saldo = 0
operacao = extrato = nome = data = logradouro = cidade = estado = exibir = continuar_listar = historico = bairro = inativar = cpf = ""
continuar_deposito = continuar_cadastro = continuar_saque = continuar_conta = continuar_inativar = "S"
usuario_lista = []
contas = []
numero_conta = 1
AGENCIA = "0001"

def cadastrar_usuario():
    global usuario, nome, data, cpf, logradouro, cidade, continuar_cadastro, historico, usuario_lista, estado, endereco, bairro, cpf
    while continuar_cadastro == "S":
        cpf = input("Digite somente os números do CPF: ")
        if cpf.isdigit() == True:
            if len(cpf) > 11:
                print("Digite somente os 11 números do CPF\n")
                continue
            elif len(cpf) < 11:
                print("Digite todos os 11 números do CPF\n")
                continue
            else:
                pass
        else:
            print("Digite somente números sem letras ou caracteres especiais\n")
            continue
        usuario = filtrar_usuario(cpf, usuario_lista)
        if usuario:
            print("Já existe um usuário com esse CPF\n")
            continue
        nome = input("Digite o nome: ")
        nome = nome.title()
        while True:
            data = input("Digite a data de nascimento dd/mm/aaaa: ")
            try:
                datetime.strptime(data, '%d/%m/%Y')
                break
            except ValueError:
                print("Data inválida, insira novamente\n")
                continue
        logradouro = input("Digite o logradouro com o número: ")
        logradouro = logradouro.title()
        bairro = input("Digite o bairro: ")
        bairro = bairro.title()
        cidade = input("Digite a cidade: ")
        cidade = cidade.title()
        while True:
            estado = input("Digite a sigla do estado: ")
            estado = estado.upper()
            if estado.isalpha() == True:
                break
            else:
                print("Digite somente letras\n")
                continue
        usuario = {"Nome" : nome, "Data de nascimento" : data, "CPF" : cpf, "Endereço" : {"Logradouro" : logradouro, "Bairro" : bairro, "Cidade" : cidade, "Estado" : estado}}
        usuario_lista.append(usuario.copy())
        print(f"Usuário {nome} registrado.\n")
        
        while continuar_cadastro != "N":
            continuar_cadastro = input("Deseja cadastrar um novo usuário? (S/N): ")
            continuar_cadastro = continuar_cadastro.upper()
            if continuar_cadastro not in "S, N":
                print("Digite SOMENTE 'S' ou 'N'\n")
                continue
            elif continuar_cadastro == "S":
                break
            else:
                break

def filtrar_usuario(cpf, usuario_lista):
    usuarios_filtrados = [usuario for usuario in usuario_lista if usuario["CPF"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None
                          

def cadastrar_conta(): 
    global continuar_conta, contas, agencia, pessoa, numero_conta, usuario

    while continuar_conta == "S": 
        if len(usuario_lista) == 0:
            print("Se cadastre antes de criar uma conta\n")
            break
        else:
            cpf = input("Digite somente os números do CPF: ")
            if cpf.isdigit() == True:
                if len(cpf) > 11:
                    print("Digite somente os 11 números do CPF\n")
                    continue
                elif len(cpf) < 11:
                    print("Digite todos os 11 números do CPF\n")
                    continue
                else:
                    pass
            else:
                print("Digite somente números sem letras ou caracteres especiais\n")
                continue
            usuario = filtrar_usuario(cpf, usuario_lista)
            if usuario:
                conta = {"Agencia" : AGENCIA , "Numero da conta" : numero_conta, "Usuario" : usuario, "CPF" : cpf}
                contas.append(conta.copy())
                numero_conta += 1
                print("Conta criada com sucesso!\n")
                pass
            else:
                print("Usuário não encontrado, tente novamente\n")
                continue
            while continuar_conta != "N":               
                continuar_conta = input("Deseja continuar cadastrando contas? (S/N): ")
                continuar_conta = continuar_conta.upper()
                if continuar_conta not in "S, N":
                    print("Insira SOMENTE 'S' ou 'N'\n")
                    continue
                elif continuar_conta == "S":
                    break
            if continuar_conta == "N": 
                break


def listar_usuarios():
    global exibir, continuar_listar, usuario_lista, usuarios, endereco, endereco_lista
    for usuario in usuario_lista:
        print("-" * 50)
        print(f"Nome: {usuario['Nome']}")     
        print(f"Data de nascimento: {usuario['Data de nascimento']}")     
        print(f"CPF: {usuario['CPF']}")     
        endereco = usuario["Endereço"]     
        print(f"Endereço: {endereco['Logradouro']} - {endereco['Bairro']}: {endereco['Cidade']}/{endereco['Estado']}\n")
        print("-" * 50)

def listar_contas():
    for conta in contas:
        linha = f"Agência: \t{conta['Agencia']}\nC/C: \t\t{conta['Numero da conta']}\nTitular: \t{conta['Usuario']['Nome']}"
        print("-" * 50)
        print(linha)
        print("-" * 50)


def inativar_conta():
    global inativar, conta, continuar_inativar
    while continuar_inativar == "S":
        inativar = input("Digite o CPF da conta que deseja excluir: ")
        if inativar.isdigit() == True:
            if len(cpf) > 11:
                print("Digite somente os 11 números do CPF\n")
                continue
            elif len(cpf) < 11:
                print("Digite todos os 11 números do CPF\n")
                continue
            else:
                pass
        else:
            print("Digite somente números sem letras ou caracteres especiais\n")
            continue
        for conta in contas:
            if conta["CPF"] == inativar:
                contas.remove(conta)
                print(f"Você inativou a conta\n")
                pass
            else:
                print("CPF não encontrado\n")
                continue
        while continuar_inativar != "N":
            continuar_inativar = input("Deseja inativar outra conta? (S/N): ")
            continuar_inativar = continuar_inativar.upper()
            if continuar_inativar not in "S, N":
                print("Digite uma opção válida, 'S' ou 'N'\n")
                continue
            elif continuar_inativar == "S":
                break
            else:
                break

def depositar():
    global saldo, continuar_deposito, extrato
    while continuar_deposito == "S":
        deposito = input("Digite o valor que deseja depositar: ")
        try:
            deposito = float(deposito)
        except ValueError:
            print("Digite um valor numérico\n")
            continue
        else:
            if deposito > 0:
                saldo += deposito
                print(f"O valor depositado foi R${deposito:.2f} e o novo saldo é R${saldo:.2f}\n")
                extrato += f"Depósito: R${deposito:.2f}\n"
                while continuar_deposito != "N":
                    continuar_deposito = input("Deseja fazer um novo deposito? (S/N): ")
                    print()
                    continuar_deposito = continuar_deposito.upper()
                    if continuar_deposito == "S":
                        break
                    else:
                        if continuar_deposito != "N":
                            print("Digite uma opção válida\n")
                            print()
                            continue
                if continuar_deposito == "N":
                        break
            else:
                print("Deposite um valor válido (acima de R$0,00)\n")
                print()
                continue
        

def sacar(): 
    global limite_saque, saldo, saque, continuar_saque, extrato
    while limite_saque <= 4:
        saque = input("Digite o valor que deseja sacar: ")
        try:
            saque = float(saque)
        except ValueError:
            print("Digite um valor numérico\n")
            print()
            continue
        if saque <= 0:
            print("Insira um valor válido, acima de 0\n")
            print()
            continue
        else:
            if saque > saldo:
                print(f"Seu saldo é insuficiente, tente um novo valor até o máximo de {saldo}\n")
                print()
                continue
            else:
                if saque <= 500:
                    saldo -= saque
                    limite_saque += 1
                    print(f'Valor R${saque:.2f} sacado\nSaldo atual: R${saldo:.2f}\n')
                    extrato += f"Saque: R${saque:.2f}\n"
                    while continuar_saque != "N":
                        continuar_saque = input("Deseja continuar sacando? (S/N): ")
                        continuar_saque = continuar_saque.upper()
                        if continuar_saque == "S":
                            break
                        else:
                            print("Digite uma opção válida\n")
                            print()
                    if continuar_saque == "N":
                            break
                else:
                    print("O limite máximo por saque é de R$500,00, tente novamente\n")
                    print()
                    continue
        if limite_saque == 3:
            print("Você atingiu o limite de saques diários, tente novamente amanhã!\n")
            print()
            break

def m_extrato(): 
    global saldo, extrato
    print("-" * 20 + " EXTRATO " + "-" * 20)
    print("Não foi realizada nenhuma transação\n" if not extrato else extrato)
    print(f"\nSaldo: R${saldo:.2f}")
    print("-" * 47)
    
    
    
print("-" * 20 + " BEM VINDO AO BANCO ARCHIE! " + "-" * 20)
while True:
    operacao = input("\nSelecione sua operação:\nU = Cadastrar Usuário\nC = Cadastrar Conta\nD = Depositar\nS = Sacar\nE = Extrato\nLC = Listar contas\nLU = Listar usuários\nI = Inativar conta\nQ = Sair\n>> ")
    operacao = operacao.upper()
    if operacao in "D, S, E, Q, U, LC, C, LU, I":
        if operacao == "D":
            continuar_deposito = "S"
            depositar()
        elif operacao == "C":
            continuar_conta = "S"
            cadastrar_conta()
        elif operacao == "U":
            continuar_cadastro = "S"
            cadastrar_usuario()
        elif operacao == "S":
            if limite_saque >= 3:
                print("Não é possível sacar mais hoje")
                print()
            else:
                sacar()
        elif operacao == "E":
            m_extrato()
        elif operacao == "LC":
            listar_contas()
        elif operacao == "LU":
            listar_usuarios()
        elif operacao == "I":
            continuar_inativar = "S"
            inativar_conta()
        else:
            print("Encerrando o programa...")
            break
    else:
        print("Insira uma opção válida, tente novamente.")
        print()
        continue