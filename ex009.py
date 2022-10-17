def Taburada(valor):
    i = 0
    while i < 11:
        print(f'{valor} * {i} = {i*valor}')
        i += 1
n1 = int(input('Digite o número e veja sua tabuada: '))


Taburada(n1)