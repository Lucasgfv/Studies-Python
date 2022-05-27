numeros = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print("Valor duplicado.")
    continuos = str(input('Quer continuar? [S/N] ').upper())
    if continuos == 'N':
        break
numeros.sort()
print(f'Você digitou os valores{numeros}')