def mult():
    b = 0
    var = int(input("Digite um numero e você tera a sua tabuada: "))
    for c in range(0, 11):
        v = var * b
        b = b + 1
        ap = v
        print(f"{var} x {b} = {ap}")
    print('Fim')
mult()