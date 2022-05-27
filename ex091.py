from random import randint
from time import sleep
from operator import itemgetter
dado = {
        'Jogador1': randint(1,6),
        'jogadro2': randint(1,6),
        'jogadrp3': randint(1,6),
        'jogador4': randint(1,6),
        'jogador5': randint(1,6),
        'jogadro6': randint(1,6)
}
final = list()
print('Valores sorteados')
for k, v in dado.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
final = sorted(dado.items(), key=itemgetter(1), reverse=True)
print(" == RANKING DOS JOGADORES == ")
for i, v in enumerate(final):
    print(f' {i+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)