#Verifique quais numeros são divisiveis por 3 ou 5 em uma escala de 1 a 100

divisor1 = 1

while divisor1 <= 100:
    if divisor1 % 3 == 0 or divisor1 % 5 == 0:
        print(f"{divisor1} é divisível por 3 e 5")
    elif divisor1 % 3 == 0:
        print(f"{divisor1} é divisível por 3")
    elif divisor1 % 5 == 0:
        print(f"{divisor1} é divisível por 5")
    divisor1 += 1