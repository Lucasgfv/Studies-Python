c = (int(input('Digite um numero: ')),
input(input('Digite outro numero: ')),
int(input('Digite mais outro numero: ')),
int(input('Digite um ultimo  numero: ')))
print(f'Os numeros digitados foram: {c}')
print(f'O valor 9 apareceu {c.count(9)} vezes.')
if 3 in c:
    print(f'O valor 3 apareceu na posição {c.index(3)+1}ª posição. ')
else:
    print('O valor 3 foi digitado em nenhuma posição.')
print(f'Os valores pares digitados forma ', end='')
for b in c:
    if b % 2 == 0:
        print(c, end=' ')