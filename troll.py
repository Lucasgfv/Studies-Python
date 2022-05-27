from random import randint
import playsound
sorteio = randint(0,5)
print('Estou pensando em um número entre 0 e 5...')
n = int(input('Adivinhe o número escolhido por mim: '))
if n == sorteio:
    print('Acertou Mizeravi!')
    playsound.playsound('acertou.mp3')
else:
    print('Errooouu')
    playsound.playsound('errou.mp3')