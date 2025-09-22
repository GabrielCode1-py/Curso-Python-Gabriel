#Crie um programa que leia a altura e o peso de um caminhão e
#verifique-se ele pode passar por um túnel.
#O túnel tem 5 metros de altura e suporta um peso maximo de 5.000kg.

altura = float(input("Digite a altura do caminhão: "))
peso = float(input("Digite o peso do caminhão (incluso carga): "))
if altura <= 5 and peso <= 5.000:
    print("Acesso liberado, altura e peso dentro do limite>")

else:
        print("Acesso negado, peso e altursa excedem o limite>")