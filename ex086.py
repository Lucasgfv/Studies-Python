matriz = [[0,0,0],[0,0,0],[0,0,0]]
for c in range(0,3):
    for l in range(0, 3):
        matriz[l] [c] = int(input(f'Difite o valor para a posição [{c}, {l}]'))
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c] [l]:^5}]', end='')
    print()
