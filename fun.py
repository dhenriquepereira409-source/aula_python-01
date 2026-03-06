def mostrar_menu():
    print("=== MENU RESTAURANTE ===")
    print("1 - VER O CARDAPIO")
    print("2 - FAZER PEDIDO")
    print("3 - VER CONTA")
    print("4 - SAIR")
    print("======================")

while True:
    mostrar_menu()
    opcao = str(input("Escolha uma opção: "))
    match opcao:
        case "1":
            print("---Cardapio---")
            print("1 Pizza - $35")
            print("2 Hamburguer - $20")
            print("3 Refrigerante - $10")
        
        case "2":
            print("\nO que deseja pedir?")
            print("1 Pizza - $35")
            print("2 Hamburguer - $20")
            print("3 Refrigerante - $10")

            pedido = int(input("Escolha: "))
            
            match pedido:

                case 1:
                    conta = 0
                    conta += 35
                    print("Pedido selecionado: Pizza ")
                case 2:
                    conta = 0
                    conta += 20
                    print("Pedido selecionado: Hamburguer ")
                case 3:
                    conta = 0
                    conta += 10
                    print("Pedido selecionado: Refrigerante ")
                case _:
                    print("Opção Invalida ")
                    
        case "3":
            print(f"\nO valor da conta: R$ {conta}")
        
        case "4":
            print("O brigado por visitar")
            break
        case _:
            print("Opção Inválida, Tente novamente.")