p = int(input('Primeiro termo de uma PA: '))
r = int(input('Razão da PA: '))
c = 1
x = p
while c <= 10:
    print('{} ->  '.format(x), end='')
    x += r
    c += 1
print('Fim')

