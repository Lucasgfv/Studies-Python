lista = []
pessoa = []
maxi = mini = 0
while True:
    lista.append(str(input("Nome: ")))
    lista.append(float(input("Idade: ")))
    lista.append(int(input("Peso: ")))
    if len(pessoa) == 0:
        maxi = mini = lista[2]
    else:
        if lista[2] > maxi:
            maxi = lista[2]
        if lista[2] < mini:
            mini = lista[2]
    pessoa.append(lista[:])
    lista.clear()
    continuar = str(input("Quer continuar? [S/N]")).upper()
    if continuar == "N":
        break
print(lista)
print(f"Ao todo, você cadastrou {len(pessoa)} pessoas")
print(f"O maior foi {maxi}KG. Peso de ", end='')
for p in pessoa:
    if p[2] == maxi:
        print(f'{p[0]}', end=', ')
print()
print(f"O menor peso foi de {mini}KG. Peso de ", end='')
for p in pessoa:
    if p[2] == mini:
       print(f'{p[0]}', end=', ')