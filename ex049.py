num = int(input('Digite um numero e você terá a tabuada dele'))
for c in range(1, 11):
    print('{} x {:2} = {}'.format(num, c, num*c))