dia = 0
maiorT = 0
diaMQ = 1
total = 0

for dia in range(1, 4):
    temperatura = float(input(f"Digite a temperatura do dia: "))
    total += temperatura
    if temperatura > diaMQ:
        diaMQ = temperatura 
        maiorT = dia 

print (f"A maior temperatura registrada foi no dia: {diaMQ}")
media = total / 3
print(f"A média foi de {media}")
