numbers = list()
pares = list()
impares = list()
while True:
    numbers.append(int(input("Digite um numero: ")))
    cont = str(input('Quer continuar? [s/n] ')).upper()
    if cont == 'N':
        break
print('-=-'*30)
print(f'A lista completa é {numbers}')
for i, v in enumerate(numbers):
    if v % 2 == 0:
        pares.append(v)
    if v % 2 != 0:
        impares.append(v)
print(f'A lista de ímpares é {impares}')
print(f'A lista de pares é {pares}')