v = 0
c = 0
soma = 0
while c != 999:
    c = int(input('Digite um numero [999 para parar]: '))
    v += 1
    soma += c
print('Você digitou {} numeros e a soma entre eles foi {}.'.format(v-1, soma-999))