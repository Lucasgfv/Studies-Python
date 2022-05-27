#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#escolhedor aleatorio
from random import choice
al1 = str(input('Digite o nome do primeiro aluno: '))
al2 = str(input('Digite o nome do segundo aluno: '))
al3 = str(input('Digite o nome do terceiro aluno: '))
al4 = str(input('Digite o nome do quarto aluno: '))
al5 = str(input('Digite o nome do quinto: '))
lista = [al1, al2, al3, al4, al5]
escolhido = choice(lista)
print('O(a) aluno(a) escolhido para apresentar o trabalho foi o(a) {}: '.format(lista))