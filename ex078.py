lista = []
maxi = 0
mini = 0
for c in range(0, 5):
    lista.append(int(input(f"Digite um numero para a possisao {c}: ")))
    if c == 0:
        maxi = mini = lista[c]
    else:
        if lista[c] > maxi:
            maxi = lista[c]
        if lista[c] < mini:
            mini = lista[c]
print(lista)
print('-'*30)
print(f"O maior valor foi {maxi} na possição ", end='')
for i, v in enumerate(lista):
    if v == maxi:
        print(f" {i}...", end='')
print()
print(f"O menor valor foi {mini} na possição ", end='')
for i, v in enumerate(lista):
    if v == mini:
        print(f" {i}...", end='')
