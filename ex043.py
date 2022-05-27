alt = float(input('Digite seua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / (alt **2)
if imc < 18.5:
    print('Seu peso esta abaixo do indicado para seu corpo. Pois, seu imc é {:.2f}.'.format(imc))
elif imc > 18.6 and (imc < 24.9):
    print('Você está no peso ideal, Parabéns! Pois, seu imc é {:.2f}.'.format(imc))
elif imc > 25.0 and (imc < 29.9):
    print('Você está levemente acima do peso. Pois, seu imc é {:.2f}.'.format(imc))
elif imc > 30.0 and (imc < 34.9):
    print('Você está com obesidade grau I. Pois, seu imc é {:.2f}.'.format(imc))
elif imc > 35.0 and (imc < 34.9):
    print('Você está com obesidade grau II (severa). Pois, seu imc é {:.2f}.'.format(imc))
elif imc > 40:
    print('Você está com obesidade III (mórbida). Pois, seu imc é {:.2f}.'.format(imc))
