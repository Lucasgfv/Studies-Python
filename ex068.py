import random
print("Jogo do par ou impar")
v = 0
while True:
    vc = int(input("Escolha um valor: "))
    pc = random.randint(0, 10)
    fin = vc + pc
    src = ' '
    while src not in 'PpIi':
        src = str(input("Par ou Impar? [p/i]")).strip().upper()
    fim = fin % 2
    if src == "P":
        if fim == 0:
            print(f"Você ganhou, parabéns! O computador escolheu {pc} e vc escolheu {vc} portato a soma foi {fin} eresultando em par.")
            v += 1
        else:
            print(f"Você perdeu! O computador escolheu {pc} e vc escolheu {vc} portato a soma foi {fin} eresultando em impar.")
            break
    elif src == "I":
        if fim == 1:
            print(f"Você ganhou, parabéns! O computador escolheu {pc} e vc escolheu {vc} portato a soma foi {fin} eresultando em impar.")
            v += 1
        else:
            print(f"Você perdeu! O computador escolheu {pc} e vc escolheu {vc} portato a soma foi {fin} eresultando em par.")
            break
print(f"Fim, você ganhou {v} vezes.")