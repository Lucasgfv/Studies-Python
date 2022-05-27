num = int(input('Digite um numero inteiro: '))
ler = int(input('Digite [1] Para converte para binario \n[2] Para octal \n[3] Para hexadecimal\n '))
if 1 == ler:
    print('O numero em Binrio é: {}'.format(bin(num[2:])))
elif 2 == ler:
    print('O numero em Octal é: {}'.format(oct(num[2:])))
elif 3 == ler:
    print('O numero em Hexadecimal é: {}'.format(hex(num[2:])))
else:
    print('Você digitou errado refaça o caminho!')