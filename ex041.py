import datetime
ano = int(input('Qual o ano de seu nacimento: '))
hoje = datetime.date.today().year
idade = hoje - ano
if idade <= 9:
    print('A categoria do(a) atleta é mirim.')
elif idade <= 14:
    print('A categoria do(a) atleta é infantil.')
elif idade <= 19:
    print('A categoria do(a) atleta é junior.')
elif idade <= 20:
    print('A categoria do(a) atleta é sênior.')
else:
    print('A categoria do(a) atleta é Mester.')