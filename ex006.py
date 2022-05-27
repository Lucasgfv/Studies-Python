#Minha resoluçao feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Exercicio que fala qual é o valor dobro, triplo e a raiz quadrada do numero digitado.
n1 = int(input('Digite um número: '))
d = n1 * 2
d2 = n1 * 3
r = n1 ** (1/2)
print('O valor digitado foi {}, o seu dobro é {}, o seu triplo {}, sua raiz quadrada é {:.2f}.'.format(n1, d, d2, r))