#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
# Crie um programa que leia o nome completo de
# uma pessoa e mostre: - O nome com todas as
# letras maiúsculas e minúsculas. - Quantas letras ao
# todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()#o .strip retira os espaços inuteis do inicio e final
print('seu nome em maiusculo é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
#
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
#ou
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0],len(separa[0])))