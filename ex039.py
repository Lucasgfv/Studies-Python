import datetime
idad = int(input('Digite o ano de seu nacimento: '))
hoje = datetime.date.today().year
temp = hoje - idad
if temp < 18:
    print('Você ainda não tem idade para se alistar no exercito.')
elif temp > 18:
    print('Você ja passou da idade de se alistar no exercito.')
elif temp == 18:
    print('Você está na idade de se alistar no exercito.')
