# Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
# Jogo de acertar um numero
import random
import time
lista = random.randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um numero entre 0 e 5. Adivinhe......')
print('-=-' * 20)
pessoa = int(input('Em que numero entre 1 a 5: '))
print('Processando........')
time.sleep(2)
if lista == pessoa:
    print('Parabens você acertou o numero esolhido pelo programa!')
else:
    print('Não foi dessa vez pois o numero escolhido pelo comptadpr foi {}.'.format(lista))
