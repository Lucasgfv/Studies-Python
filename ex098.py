import time
def counter():

    print('-=-' * 30)
    print("Contagem de 1 até 10 de 1 em 1")
    for c in range(1, 11, 1):
        time.sleep(0.5)
        print(f"{c} ", end='')
        if c == 10:
            print("Fim!")
    print('-=-' * 30)
    print("Contagem de 10 até 0 de 2 em 2")
    for v in range(10, -1, 2):
        time.sleep(0.5)
        print(f"{v} ", end='')
        if v == 0:
            print("Fim!")
    for cont in range(start, endf, step):
        time.sleep(0.5)
        print(f"{cont} ", end="")
        if cont



counter()
print('-=-' * 30)
print("Agora é sua vez de personalizar a contagem!")
start = int(input("Start: "))
end = int(input("End: "))
step = int(input("Step: "))
print('-=-' * 30)





