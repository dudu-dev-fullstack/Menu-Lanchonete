print("[1] Lache")
print("[2] Bebida")
print("[3] Sobremesa")
print("[4] Sair")
opc = int(input("Escolha uma opcao: "))

match opc:
    case 1:
        print("[1] Cachorro quente: 20R$")
        print("[2] Hamburguer: 30R$")
        Lanche = int(input("Escolha um dos lanches: "))
        if Lanche == 1:
            ch = int(input("Quantos você deseja? "))
            print(f"O valor total é: {ch*20}")
        elif Lanche == 2:
            hb = int(input("Quantos você deseja? "))
            print(f"Você terá que pagar {hb*30}R$")
        else:
            print("Você digitou uma opcao invalida!")
    case 2:
        print("[1] Refrigerante: 12R$")
        print("[2] Suco: 6R$")
        Bebida = int(input("Escolha uma das bebidas: "))
        if Bebida ==1:
            rf = int(input("Quantos você deseja?: "))
            print(f"Você terá que pagar {rf*12}R$")
        elif Bebida ==2:
            sc = int(input("Quantos você deseja?: "))
            print(f"Você terá que pagar {sc*6}R$")
        else:
            print("Você digitou uma opcao invalida!")
    case 3:
        print("[1] Sorvete: 15R$")
        print("[2] Bolo: 8R$")
        Sobremesa = int(input("Escolha uma das sobremesas: "))
        if Sobremesa == 1:
            sv = int(input("Quantos você deseja?: "))
            print(f"Você terá que pagar {sv*15}R$")
        elif Sobremesa == 2:
            bl = int(input("Quantos você deseja?: "))
            print(f"Você terá que pagar {bl*8}R$")
        else:
            print("Opcao invalida!")
    case 4:
        print("Obrigado volte sempre!")
    case _:
        print("Opcao invalida!")