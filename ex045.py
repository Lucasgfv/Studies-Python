import random
import time
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0, 2)
print('''Suas opições: 
[0]Tesoura
[1]Pedra 
[2]Papel ''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PO!!!')
time.sleep(0.5)
print('-='*12)
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-='*12)
if computador == 0: #Pedra
    if jogador == 0:
        print('Empate')
    elif jogador == 1:
        print('Jogador vence')
    elif jogador == 2:
        print('Computador vence')
    else:
        print('Jogada invalida!')
elif computador == 1: #Papel
    if jogador == 0:
        print('Computador vence')
    elif jogador == 1:
        print('Empate')
    elif jogador == 2:
        print('Vence')
    else:
        print('Jogada invalida!')
elif computador == 2: #Tesoura
    if jogador == 0:
       print('Jogador vence')
    elif jogador == 1:
         print('Computaador vence')
    elif jogador == 2:
          print('empate')
    else:
        print('Jogada invalida!')