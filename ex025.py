#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Digite seu nome copleto: ')).strip()
print('Seu nome tem Silva:{}'.format('silva' in nome.lower()))