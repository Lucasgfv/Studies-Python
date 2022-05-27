numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
print(f'Os valores pares são {numeros[0]}.')
print(f'Os valores impares são {numeros[1]}')