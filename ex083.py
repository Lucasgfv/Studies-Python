par = str(input('Digite a expresão: '))
pilha = []
for c in par:
    if c == '(':
        pilha.append('(')
    elif c == (')'):
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressao esta valida!')
else:
    print('Sua expressao esta invalida!')