#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
velocidade = int(input('Qual a velocidade do carro em km/h: '))
if velocidade >= 80:
    multa = (velocidade - 80) * 7
    print('Você ultrapassou o limite, está multado, sua multa é de R${},00 reais!'.format(multa))
else:
    print('Parabens você esta obedecendo a lei continue assim.')