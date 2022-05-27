n1 = float(input('Digite a pprimeira nota: '))
n2 = float(input('Digite a sugunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua media foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! Esrude mais!')

nome = str(input('Qual é o seu nome? '))
if nome == 'Lucas':
    print('Parabens seu idiota se fudeu, trouxa.')
else:
    print('Ola, tenha um bom dia!')
print('Acabou o programa.')