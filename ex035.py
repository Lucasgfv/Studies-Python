#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
a = float(input('Diga para mim o primeiro comprimeto: '))
b = float(input('Diga o segundo lado: '))
c = float(input('Diga o terceiro lado: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('É possivel sim que esse trinagulo exista.')
else:
    print('Não é possivel formar um triangulo com as medidas dadas.')