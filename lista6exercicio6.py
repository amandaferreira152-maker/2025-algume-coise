num_produtos = int(input("Quantos produtos foram comprados? "))

total_geral = 0
total_alimenticios = 0
total_outros = 0

for i in range(1, num_produtos + 1):
    valor = float(input(f"Digite o valor do produto {i}: "))
    tipo = int(input(f"O produto {i} é alimentício (1) ou outro tipo (2)? "))

    total_geral += valor

    if tipo == 1:
        total_alimenticios += valor
    elif tipo == 2:
        total_outros += valor
    else:
        print("Tipo inválido, o produto será considerado como outro tipo.")
        total_outros += valor

print("\nResumo da compra:")
print(f"Total geral: R$ {total_geral:.2f}")
print(f"Total de produtos alimentícios: R$ {total_alimenticios:.2f}")
print(f"Total de outros produtos: R$ {total_outros:.2f}")
