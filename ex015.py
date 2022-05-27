#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#Execici de aluguel de carro
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))