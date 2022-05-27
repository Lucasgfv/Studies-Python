inicio = s = cont = 0
while True:
    inicio = int(input('Digite um valor: '))
    if inicio == 999:
        break
    s += inicio
    cont += 1
print(f"Foi digitado {cont} numeros e a soma entre eles foi de {s}.")