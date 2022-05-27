#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade = str(input('Em qual cidade voce mora: ')).strip()
print(cidade[:5].upper() == 'SANTO')