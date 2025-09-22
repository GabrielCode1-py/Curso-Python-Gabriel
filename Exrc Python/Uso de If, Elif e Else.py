#Uso de If, Elif e Else.
#Crie um programa que leia a nota do aluno, se a nota
#for 90 "Conceito A: Excelente, 80 "Conceito B: Bom, 70 "Conceito C: Regular, 60 "Conceito D: Insuficiente, 50 "Conceito E: Reprovado.

nota1= float(input("Digite a nota do aluno: "))

if nota1>= 90:
    print("Conceito A: Excelente")

elif nota1>= 80:
    print("Conceito B: Bom")

elif nota1>= 70:
    print("Conceito C: Regular")

elif nota1>= 60:
    print("Conceito D: Insuficiente")

else:
    print("Conceito E: Reprovado")


