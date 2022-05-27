numeros = list()
while True:
    numeros.append(int(input('Digite um valor: ')))
    continuos = str(input("quer continuar? [n/s] ")).upper()
    if continuos == 'N':
        print(f'Você digitou {len(numeros)} numeros')
        break
if 5 in numeros:
    print('O valor 5 faz parte da lista.')
else:
    print('O valor 5 não faz parte da lista.')
numeros.sort(reverse = True)
print(f'Os valores adicionados em ordem decrescente são {numeros}')
