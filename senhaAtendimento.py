ordem_senhasNormal = []
ordem_senhasPrioridade = []

n_senhaNormal = 0
n_senhaPrioridade = 0

def verificar_ordem():
    print("Senhas ATENDIMENTO NORMAL: ")
    print(f"{ordem_senhasNormal}")

def senha_normal():
    global n_senhaNormal

    n_senhaNormal += 1
    ordem_senhasNormal.append({
        "Nº": n_senhaNormal,
    })
    print(f"Senha: Nº{n_senhaNormal}")

    retornar_menu = input("Pressione enter pra voltar ao menu principal: ")

    return main_menu()

def senha_prioridade():
    global n_senhaPrioridade

    n_senhaPrioridade += 1
    ordem_senhasPrioridade.append(n_senhaPrioridade)
    print(f"Senha: Pº{n_senhaPrioridade}\n")

    retornar_menu = input("Pressione enter pra voltar ao menu principal: ")

    return main_menu()

def main_menu():
    print("\n *** BEM-VINDO AO GERADOR DE SENHA DE ATENDIMENTO *** \n")
    print("Por favor, selecione a categoria que você se enquadra: \n")
    print("1. ATENDIMENTO NORMAL")
    print("2. PRIORIDADE (IDOSOS, DEFICIENTES OU GESTANTES)")
    print("3. VER SENHAS EMITIDAS\n")
    opcao_menu = int(input("Opção: "))

    if opcao_menu == 1:
        senha_normal()
    elif opcao_menu == 2:
        senha_prioridade()
    elif opcao_menu == 3:
        verificar_ordem()
    

while True:
    main_menu()
    