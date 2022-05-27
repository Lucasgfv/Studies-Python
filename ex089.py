lista = list()
while True:
    nome = str(input("Nome: "))
    Nota1 = float(input("Nota 1: "))
    Nota2 = float(input("Nota 2: "))
    media = (Nota1 + Nota2) / 2
    lista.append([nome,[Nota1, Nota2], media])
    continuar = str(input("Quer continuar? ")).upper()
    if continuar == "N":
        break
print('-'*30)
print(f'{"No":<4}{"Nome":<10}{"Media":>8}')
print('-'*30)
for i, l in enumerate(lista):
    print(f"{i:<4}{l[0]:<10}{l[2]:>8.1f}")
print("-"*30)
while True:
    detalhe = int(input("Mostrar nota de qual aluno? (999 interrompe) "))
    if detalhe == 999:
        break
    if detalhe <= len(lista) -1:
        print(f" As notas de {lista[detalhe][0]} são {lista[detalhe][1]}")