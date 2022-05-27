nota = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
med = (nota + nota2) / 2
if med <= 5.0:
    print('O aluno está reprovado pois sua media foi {}.'.format(med))
elif med >= 5.0 and med <= 6.9:
    print('O aluno está de recuperação pois sua media foi {}'.format(med))
elif med >= 7.0:
    print('O aluno está aprovado pois sua media foi {}.'.format(med))