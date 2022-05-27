pro = float(input('Digite o valor de seu produto: '))
pag = int(input('Qual o meio de pagamento?\n [1] para dinheiro/cheque\n [2] para pagamento a vista no cartão com 5% de desconto,\n [3] para parcelado no cartão sem juros,\n [4] para pagamento parcelado em 3x ou mais no cartão com 20% de juros.\n'))
if pag == 1:
    av = (pro - (pro * 10) / 100)
    print('Você selecionou no metodo de pagamento dinheiro/cheque a vista o valor a ser pago será de: R${}.'.format(av))
elif pag == 2:
    avd = (pro - ((pro * 5) / 100))
    print('Você selecionou no metodo de pagamento a vista no cartão com 5% de desconto e o valor a ser pago será de: R${}.'.format(avd))
elif pag == 3:
    pard2 = (pro / 2)
    fin = pard2 * 2
    print('Você selecionou no metodo de pagamento parcelado no cartão sem juros e o valor de cada parcela será de: R${}. Com o total final de R${}.'.format(pard2, fin))
elif pag == 4:
    pard3 = ((pro * 20) / 100) + pro
    tot = int(input('Quantas parcelas? '))
    parcelas = pard3 / tot
    print('Você selecionou no metodo de pagamento parcelado em {}x no cartão com 20% de juros e o valor de cada parcela será de: R${}. Com o total final de R${}.'.format(tot, parcelas, pard3))
