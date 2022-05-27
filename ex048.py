soma = 0
con = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        con = con + 1
print('A soma dos {} valores é: {}'.format(con, soma))