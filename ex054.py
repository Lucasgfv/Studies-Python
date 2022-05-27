import datetime
hoje = datetime.date.today().year
totalma = 0
totalme = 0
for c in range (1, 8):
    ano = int(input('Em que ano a {}º pessoa nasceu? '.format(c)))
    idad = hoje - ano
    if idad >= 21:
        totalma += 1
    else:
        totalme += 1
print('Ao todo tivemos {} pessoas maiores de idade.'.format(totalma))
print('E também tivemos {}  pessoas menores de idade.'.format(totalme))
