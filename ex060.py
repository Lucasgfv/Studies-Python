import math
r = 'S'
while r == 'S':
    fat = int(input('Digite um numero e veja seu fatorial: '))
    c = math.factorial(fat)
    print('O fatoria do numero digitado é {}'.format(c), end='')
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')