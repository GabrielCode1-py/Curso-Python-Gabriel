#Crie um programa que leia a nota de um aluno 
# e verifique se ele foi aprovado, reprovado ou 
# está de recuperação.

nomeAluno = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
notaMedia = (nota1 + nota2 + nota3) / 3

if notaMedia >= 7:
    print(f"{nomeAluno} foi aprovado com média {notaMedia:.2f}")

elif notaMedia >= 5:
    print(f"{nomeAluno} está de recuperação com média {notaMedia:.2f}")

else:
    print(f"{nomeAluno} foi reprovado com média {notaMedia:.2f}")
