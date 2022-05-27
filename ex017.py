#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#calculando a hipotenusa
import math
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#ou
co2 = float(input('Comprimento do cateto oposto: '))
ca2 = float(input('Comprimento do cateto adjacente: '))
hi2 = math.hypot(co2, ca2)
print('A hipotenusa vai medir {:.2f}'.format(hi2))

