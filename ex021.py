#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#exercicio de tocar musica no python
from pygame import mixer
mixer.init()
mixer.music.load('ex021.mp3')
mixer.music.play()
input('Agora você escuta?')