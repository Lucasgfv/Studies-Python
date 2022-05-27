pessoa = dict()
partidas = list()
time = list()
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome do jogador: "))
    jogos = int(input(f"Quantas partidas {pessoa['Nome']} Jogou? "))
    partidas.clear()
    for c in range(0, jogos):
        partidas.append = int(input(f"Quantos gols na partida {c +1}? "))
    pessoa['gols'] = partidas[:]
    pessoa['Total'] = sum(partidas)
    time.append(pessoa.copy())
    while True:
        continuar = str(input("Quer continuar?[S/N] ")).upper() [0]
        if continuar in 'SN':
            break
    if continuar == "N":
        break
print("-"*40)
print('cod', end='')
for i in pessoa.keys():
    print(f'{i:<15}', end='')
print()
print('-'*40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-'*40)
while True:
    busca = int(input('Mostra dados de qual jogador? (999 para parar)'))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRo! Não existe jogador com codigo {busca}!')
    else:
        print(f'--Levantamento do jogador {time[busca]["nome"]}:')
        for i,g in enumerate(time[busca]['gols']):
            print(f' No jogo {i+1}fez {g} gols.')
        print('-'*40)