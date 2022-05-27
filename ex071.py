sac = int(input("Quanto você quer sacar? "))
total = sac
ced = 50
toced = 0
while True:
    if total >= ced:
        total -= ced
        toced += 1
    else:
        print(f"Total de  {toced} cedulas de R${ced}.")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced ==  10:
            ced = 1
        if total == 0:
            break