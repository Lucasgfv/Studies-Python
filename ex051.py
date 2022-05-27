an = int(input('Qua é o primeiro termo de sua pa: '))
r = int(input('Qual é a razão de sua pa: '))
n = an + (10 - 1 ) * r #formula do enezimo termo de uma pa
for c in range(an, n, r):
    print('{}'.format(c), end=', ')
print('Fim')
