import random
jogo = list()
final = list()
cont = 0
tot = 1
print('-='*30)
print("              Jogo na mega sena")
print('-='*30)
var = int(input("Quantos jogos você quer que eu sorteie? "))
while tot <= var:
    cont = 0
    while True:
        num = random.randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            cont += 1
        if cont >= 6:
            break
    jogo.sort()
    final.append(jogo[:])
    jogo.clear()
    tot += 1
for i, l in enumerate(final):
    print(f'Jogos {i+1} {l}')