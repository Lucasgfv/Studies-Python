import random
lista = random.randint(0, 10)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 10. Adivinhe...')
print('-=-' * 20)
lol = 0
acertou = False
while not acertou:
    pessoa = int(input('-> '))
    lol += 1
    if pessoa == lista:
        acertou = True
    else:
        if pessoa < lista:
            print('Mais... Tente novamente: ')
        elif pessoa > lista:
            print('Menos... Tente novamente: ')
print('Parabéns você acertou e para isso você tentou {} vezes'.format(lol))