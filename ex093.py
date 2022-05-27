jogador = dict()
lista = list()
lista_final = list()
soma = 0
jogador['Nome'] = str(input("Nome do jogadro: "))
part = int(input(f"Quantas partidas {jogador['Nome']} jogou? "))
for c in range(part):
    gol = int(input(f"Quantos gols na partida {c}? "))
    soma += gol
    lista.append(gol)
    lista_final.append(lista[:])
    lista.clear()
jogador['Gols'] = lista_final
jogador['Total'] = soma
print('-=-'*30)
print(jogador)
print('-=-'*30)
print(lista_final)
for k, v in jogador.items():
    print(f"O campo {k} tem o valor {v}")
print('-=-'*30)
print(f"O jogadro {jogador['Nome']} jogou {part} partidas.")
for i, l in enumerate(lista_final):
    print(f" => Na partida {i}, fez {l} gols.")
print(f'Foi um total de {soma} gols')