p = int(input('Primeiro termo de uma PA: '))
r = int(input('Razão da PA: '))
c = 1
x = p
v = 0
g = 10
while g != 0:
    v += g
    while c <= v:
        print('{} ->  '.format(x), end='')
        x += r
        c += 1
    print('Stop')
    g = int(input('Quantos termos você que mostra mais? '))
print('Fim')

