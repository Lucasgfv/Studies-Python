#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
distancia = int(input('Digite a distancia de sua viagem Km: '))
if distancia >= 200:
    preço = distancia * 0.45
    print('O preço de sua viagem é de R${}0:'.format(preço))
else:
    preço2 = distancia * 0.50
    print('O preço de sua viagem é de R${}0'.format(preço2))
