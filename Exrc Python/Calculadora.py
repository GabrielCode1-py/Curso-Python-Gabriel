
while True:
    opcao1 = input("Digite: \n1) Adição\n2) Subtração\n3) Multiplicação\n4) Divisão\n5) Sair: \n")

    if opcao1 == "1":
        soma1 = float(input("Digite o primeiro número: "))
        soma2 = float(input("Digite o segundo número: "))
        print("O resultado é: ", soma1 + soma2)

    
    elif opcao1 == "2":
        soma1 = float(input("Digite o primeiro número: "))
        soma2 = float(input("Digite o segundo número: "))
        print("O resultado é: ", soma1 - soma2)
        
    elif opcao1 == "3":
        soma1 = float(input("Digite o primeiro número: "))
        soma2 = float(input("Digite o segundo número: "))
        print("O resultado é: ", soma1 * soma2)

    elif opcao1 == "4":
        soma1 = float(input("Digite o primeiro número: "))
        soma2 = float(input("Digite o segundo número: "))
        if soma2 == 0:
            print("Valor indeterminado")
        else:
            print("O resultado é: ", soma1 / soma2)
     
    elif opcao1 == "5":
        print("Você saiu!")
        break
    else:
        print("Opção inválida!")