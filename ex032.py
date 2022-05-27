#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
ano = int(input('Escreva o ano em que você esta: '))
if ano % 4 == 0 and ano % 100!= 0 or ano % 400 ==0:
    print('Seu ano é bissesto: ')
else:
    print('Seu ano não é bissesto. ')