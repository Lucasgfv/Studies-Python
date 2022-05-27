#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
#026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A apareceu {} vezes na frase.'.format(frase.count('A')))
print('a primeira letra A apareceu na possição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na possção {}'.format(frase.rfind('A')+1))