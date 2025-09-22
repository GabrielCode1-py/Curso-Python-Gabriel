#Álcool ou gasolina? Faça um programa para descobrir se o álcool é vantajoso ou
#não em relação à gasolina. O cálculo é dividir o preço do litro do álcool pelo da
#gasolina. Se o resultado for inferior a 0,7, use álcool. Se for maior que 0,7, então a
#gasolina é melhor.#

gasolina = float(input("Digite o preço da gasolina: "))
alcool = float(input("Digite o preço do ácool: "))

somaLitro = alcool / gasolina

if somaLitro < 0.7:
    print("O alcool é mais vantajoso.")

else:
    print("A gasolina é mais vantajoisa.")