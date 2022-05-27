while True:
    tab = int(input("Digite um valor e você tera a sua tabuada: "))
    if tab < 0:
        break
    for c in range(1, 11):
        print(f"{tab} x {c} = {tab * c}")
print("Fim")
