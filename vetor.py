# Crie dois vetores para armazenar as cidades e estados. apenas dois de cada.

cidades = []
estados = []

print("Digite 2 cidades:")
for i in range(2):
    cidades.append(input(f"Cidade {i+1}: ").strip())

print("\nDigite 2 estados (UF ou nome completo):")
for i in range(2):
    estados.append(input(f"Estado {i+1}: ").strip())

print("\nCidades e Estados informados:")
for i in range(2):
    cidade = cidades[i] if i < len(cidades) else ""
    estado = estados[i] if i < len(estados) else ""
    print(f"{i+1}. {cidade} - {estado}")
