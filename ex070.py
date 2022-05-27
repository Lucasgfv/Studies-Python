total = tomail = menor = cont = 0
barato = ''
while True:
    produto = str(input("Nome do produto: "))
    preço = float(input("preço: R$"))
    cont += 1
    total += preço
    if preço > 1000:
        tomail += 1
    if cont == 1 or preço < menor:
        menor = preço
        barato = produto
    resp = ' '
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print("Fim do programa.")
print(f"O total da compra foi R${total:.2f}")
print(f"Temos {tomail} produtos custando mais de R$1000.00")
print(f"O produto mais barato foi {barato} que custa R${menor:.2f}")