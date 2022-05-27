#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Calculador de angulo
import math
ângulo = float(input('Digite o angulo que você deseja: '))
seno = math.sin(math.radians(ângulo))#(radians) é a converção para radianos
print('o ângulo de {} tem o seno de {:.2f}'.format(ângulo, seno))
cosseno = math.cos(math.radians(ângulo))
print('o ângulo de {} tem o cosseno de {:.2f}'.format(ângulo, cosseno))
tangente = math.tan(math.radians(ângulo))
print('O ângulo de {} tem a tangente de {:.2f}'.format(ângulo, tangente))