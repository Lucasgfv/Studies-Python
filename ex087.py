matriz = [[0,0,0], [0,0,0], [0,0,0]]
g = maxi = mini = 0
for c in range(0,3):
    for l in range(0,3):
        matriz[l] [c] = int(input(f'[{c}, {l}]'))
print('=*'*15)
for c in range(0,3):
    for l in range(0,3):
        print(f'[{matriz[c] [l]:^5}]', end='')
        if matriz [c] [l] % 2 ==0:
             g += matriz[c] [l]
    print()
print('=*'*15)
print(f'A soma dos valores pares são {g}')
for c in range(0,3):
    maxi += matriz[c][2]
print(f'A soma dos valores da terceira coluna é {maxi}')
for l in range(0,3):
    if l == 0:
        mini = matriz[1][l]
    elif matriz[1][l] > mini:
        mini = matriz[1][l]
print(f'O maior valor da segunda linha é {mini}')