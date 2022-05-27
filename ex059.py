import time
r = 'S'
numum = int(input('Digite um numero inteiro: '))
numdois = int(input('Digite outro numero:'))
escolha = 0
while escolha != 5:
    print('''[1] Somar
    [2] Multiplicador
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    escolha = int(input('Qual a sua opção '))
    if escolha == 1:
        soma = numum + numdois
        print('A soma dos dois valores da {}'.format(soma))
    elif escolha == 2:
        mult = numum * numdois
        print('A multiplicação dos valores é {}'.format(mult))
    elif escolha == 3:
        if numum > numdois:
            print('O primeiro valor digitado é maior que o segundo.')
        else:
            print('O segundo valor digitado é maior se comparado com o primeiro.')
    elif escolha == 4:
            numum = int(input('Digite um numero inteiro: '))
            numdois = int(input('Digite outro numero: '))
    elif escolha == 5:
        print('Finalizando........')
        time.sleep(1)
    else:
        print('Opção invalida tente novamente: ')
print('Fim do programa, obrigado por participar.')