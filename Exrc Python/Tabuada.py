print("====| TABÚADA |====\n")

while True:
    # Solicita o número para a tabuada
    tabuada = int(input("Digite um número: "))

    print(f"Tabuada de {tabuada}: ", end="")

    #Loop para mostrar a tabuada de 1 a 10
    num = 1
    while num <= 10:
        resultado = tabuada * num
        print(f"{tabuada} x {num} = {resultado}", end= "   ")
        num += 1
