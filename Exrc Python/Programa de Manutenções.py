# Faça um algoritmo que leia um conjunto de 5 manutenções, um de cada vez, acompanhados
# de um código 1, 2 ou 3. Este valor representa o código das peças utilizadas em uma das 5
# manutenções feitas e os códigos representam: Motor 12v, Resitor de 200Ω e Capacitor de 100μF.
# • Deve aparecer a tabela para o usuário visualizar o código das peças e o nome da peça. Use
# símbolos gráficos como *,-,=,#,| para deixar a tabela organizada visualmente.
# • Utilize o Escolha ... caso para escolher o código da peça e digitar a quantidade de
# manutenções daquela peça.
# • Mostre no final
# o total geral de peças utilizadas
# o total de Motor 12V
# o total de Resistor 200Ω
# o total de Capacitores de 100 μF
# o percentual de Motor, de Resistor e de Capacitor.

#Determinar as váriaveis e as listas
equipamentos = ["Motor - 12v", "Resistor - 200Ω", "Capacitor - 100μF"] #lista de equipamentos
contadores = [0,0,0] #Armazena toda vez que um número for digitada, numero de 1 a 4
manutencoes = 0 #variavél que irá armazenar cada vez que o usuário selecionar uma opção para calcular total no final.
rodando = True  #enquanto "rodando for igual a Verdade/True, o programa rodara até chegar em X quantidades determinadas."

while manutencoes < 10 and rodando:   #Laço de loop
    print("=====| [SISTEMA DE MANUTENÇÃO] |=====")
    #mostrar menu
    for i, item in enumerate(equipamentos, start=1):
        print(f"[{i}] {item:<16}")
    print("[4] Sair")
        
    opcao = int(input("\nEm qual equipamento será feita a manutenção?: "))
    
    #Condicionais para o programa rodar.
    if 1 <= opcao <= 3:
        escolhido = equipamentos[opcao - 1]
        confirmar = input(f"Confirmar manutenção em {escolhido}? sim/nao): \n").lower()
        if confirmar == "sim":
            contadores[opcao - 1] += 1
            manutencoes += 1
            print(f"\nReparo feito com sucesso em {escolhido}\n")
        else:
            print("\nManutenção cancelada.\n")
    elif opcao == 4:
        print("Obrigado por usar o nosso sistema!")
        rodando = False
    

    #Calculo das quantidade de manutenções feitas e suas respectivas porcentagens.

total = sum(contadores)
if total > 0:
    print("\n====| ° RESUMO DE MANTENCÕES ° |====")
    for i, qtd in enumerate(contadores):
        porcentagem = (qtd * 100) / total
        print(f"{equipamentos[i]}: {qtd} Manutenções ({porcentagem: .2f}%)")