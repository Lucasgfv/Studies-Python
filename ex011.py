#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Calculado a area de uma parede para ver quanto de tinta sera necessario para pinta-la
n1 = float(input('Qual é a altura de sua parede em metros: '))
n2 = float(input('Qual é a largura de sua parede em metros: '))
a = n1 * n2
t = a / 2
print('A área de sua parede é de {} metros e para pinta-la por completo você precissara de {} litros de tinta.'.format(a, t))