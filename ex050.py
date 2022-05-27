lol = 0
soma = 0
for f in range(1, 7):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
         lol = lol + f
         soma = soma + 1
print('Você digitou {} numeros pares e a soma deles é{}'.format(lol, soma))