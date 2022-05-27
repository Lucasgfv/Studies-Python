#Minha resolução feita das atividades exigidas do Curso de PYthon do canal do youtube Curso em Video apresentado pelo prfessor Gustavo Guanabara
valor = float(input('Qual o valor da casa que você desseja comprar? '))
sal = float(input('Qual é o valor do seu salario? '))
ano = float(input('Em quantos anos você desseja pagar seu imovel? '))
mes = ano * 12
parcela = valor / mes
sal2 = (sal * 30) / 100
if sal2 <= parcela:
    print('Seu emprestimo foi reprovado pois a sua parcela é superior a 30% de seu salario.')
else:
    print('Parabens seu emprestimo foi aprovado e suas parcelas seram de R${:.2f}'.format(parcela))