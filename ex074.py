import random
c = random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10)
print('Os valores sorteados foram: ', end='')
for n in c:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(c)}.')
print(f'O menor valor sorteado foi {min(c)}.')
