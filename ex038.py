pri = int(input('Digite um numero inteiro: '))
seg = int(input('digite um outro valor inteiro: '))
if pri == seg:
    print('Não existe valor maior, os dois são iguais.')
elif pri > seg:
    print('O primeirro valor digitado por você foi maior que o segundo.')
else:
    print('O segundo valor digitado por você foi maior que o primeiro.')