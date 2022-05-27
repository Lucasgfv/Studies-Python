cont = h = mu = 0
while True:
    print("-------------------")
    print("Cadastre uma pessoa")
    print("-------------------")
    idade = int(input("Qual a sua idade? "))
    sexo = str(input("Qual o seu sexo [M/F]? ")).strip().upper()[0]
# Pessoa maior ou igual a 18 anos
    if idade >= 18:
        cont += 1
# Homem
    if sexo == "M":
        h += 1
# Mulher maior ou igual a 20 anos
    if sexo == "F" and idade >= 20:
        mu += 1
    print("-------------------")
    con = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if con == "N":
        break
print(f"Total de pessoas cadastradas com mais de 18 anos: {cont}")
print(f"Ao todo temos {h} homens cadastrados.")
print(f"E temos {mu} mulheres com menos de 20 anos.")