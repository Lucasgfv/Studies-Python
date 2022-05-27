v = 's'
b = cont = media = maior = menor = 0
while v in 's':
    c = int(input('Digite um numero: '))
    cont += 1
    b += c
    if cont == 1:
        c = maior = menor
    else:
        if c > maior:
            maior = c
        if c < menor:
            menor = c
    v = str(input('Quer continuar? [s/n]'))
media = b / cont
print('Você digitou {} numeros e a media foi {}.'.format(cont, media))
print('O maior valor foi {} e o menor foi {}.'.format(maior, menor))