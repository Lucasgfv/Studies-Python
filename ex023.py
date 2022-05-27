#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
n = int(input('Digite um numero entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Analisando o munero {}....... '.format(n))
print('Unidade: {} '.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))