numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'trze', 'quatorze', 'quinze', 'deseseis', 'deseste', 'dezoito', 'dezenove', 'vinte')
while True:
    num = int(input("Digite um numero: "))
    if 0 <= num <= 20:
        break
    print("Numero nao encontrado digite novamente....", end ='')
print(f"O valor digitado foi {numeros[num]}.")

