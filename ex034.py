#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
salario = float(input('Qual é o seu salario? '))
if salario >= 1250.00:
    fin = ((salario * 10) / 100) + salario
    print('Seu aumento é de 10% isso siguinifica que seu salario passará a ser de R${}.'.format(fin))
else:
    fin2 = ((salario * 15) / 100) + salario
    print('Seu aumento é de 15% isso siguinifica que seu salario passará a ser de R${}'.format(fin2))