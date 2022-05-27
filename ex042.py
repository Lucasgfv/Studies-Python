a = float(input('Diga para mim o primeiro comprimeto: '))
b = float(input('Diga o segundo lado: '))
c = float(input('Diga o terceiro lado: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('É possivel sim que esse trinagulo exista')
    if(a == b == c):
        print('Ele será equilatero.')
    elif(a != b != c != a):
        print('Ele será escaleno.')
    else:
        print('Ele será isósceles.')
else:
    print('Não é possivel formar um triangulo com as medidas dadas.')
