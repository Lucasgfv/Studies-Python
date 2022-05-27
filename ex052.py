num = int(input('Digite um mnumero inteiro e veja se ele é primo ou não: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:#divisivel
        print('\033[33m', end='')
        tot = tot + 1
    else:#não divisivel
        print('\033[31m',end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisivel {} vezes.'.format(num, tot))
if tot == 0:
    print('O numero é primo.')
else:
    print('O numero não é primo.')